from collections import defaultdict,deque
from datetime import datetime,timezone
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy import delete,select
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import settings
from app.database import get_db
from app.dependencies import get_current_user
from app.models.conversation import AIConversation,AIMessage
from app.models.user import User
from app.schemas.ai import AIChatRequest,AIChatResponse,CodeRequest,ConversationPublic,DebugRequest,GenerateRequest,ImproveRequest,MessagePublic,TeachRequest
from app.services.gemini_service import generate_developer_response
router=APIRouter(prefix='/api/ai',tags=['AI Assistant']);request_log=defaultdict(deque)
def enforce_rate(user_id:int):
    now=datetime.now(timezone.utc).timestamp();items=request_log[user_id]
    while items and now-items[0]>60:items.popleft()
    if len(items)>=settings.ai_rate_limit_per_minute:raise HTTPException(429,'Too many AI requests. Please wait a moment.')
    items.append(now)
async def conversation(db,user_id,conversation_id,message):
    item=await db.get(AIConversation,conversation_id) if conversation_id else None
    if not item or item.user_id!=user_id:item=AIConversation(user_id=user_id,title=message[:80]);db.add(item);await db.flush()
    return item
@router.post('/chat',response_model=AIChatResponse)
async def chat(payload:AIChatRequest,db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):
    enforce_rate(user.id);conv=await conversation(db,user.id,payload.conversation_id,payload.message);answer=await generate_developer_response(payload.message,payload.html_code,payload.css_code,payload.javascript_code);db.add_all([AIMessage(conversation_id=conv.id,role='user',content=payload.message),AIMessage(conversation_id=conv.id,role='assistant',content=answer)]);await db.commit();return {'response':answer,'conversation_id':conv.id,'model':settings.gemini_model if settings.gemini_api_key else 'demo','timestamp':datetime.now(timezone.utc)}
async def specialized(prompt,user,db):
    enforce_rate(user.id);return await generate_developer_response(prompt)
@router.post('/explain-code')
async def explain(payload:CodeRequest,db=Depends(get_db),user=Depends(get_current_user)):return {'response':await specialized(f'Explain this {payload.language} code for a beginner:\n{payload.code}',user,db)}
@router.post('/debug-code')
async def debug(payload:DebugRequest,db=Depends(get_db),user=Depends(get_current_user)):return {'response':await specialized(f'Debug this {payload.language} code. Error: {payload.error}\nCode:\n{payload.code}',user,db)}
@router.post('/improve-code')
async def improve(payload:ImproveRequest,db=Depends(get_db),user=Depends(get_current_user)):return {'response':await specialized(f'Improve this web project for readability, accessibility, responsiveness, and performance. HTML:{payload.html_code} CSS:{payload.css_code} JS:{payload.javascript_code}',user,db)}
@router.post('/generate-code')
async def generate(payload:GenerateRequest,db=Depends(get_db),user=Depends(get_current_user)):return {'response':await specialized(f'Generate a complete web development example for: {payload.request}',user,db)}
@router.post('/teach')
async def teach(payload:TeachRequest,db=Depends(get_db),user=Depends(get_current_user)):return {'response':await specialized(f'Teach the web-development concept {payload.concept} with a practical example.',user,db)}
@router.post('/review-project')
async def review(payload:ImproveRequest,db=Depends(get_db),user=Depends(get_current_user)):return {'response':await specialized(f'Review this project and give actionable improvements. HTML:{payload.html_code} CSS:{payload.css_code} JS:{payload.javascript_code}',user,db)}
@router.get('/conversations',response_model=list[ConversationPublic])
async def conversations(db=Depends(get_db),user=Depends(get_current_user)):return list((await db.scalars(select(AIConversation).where(AIConversation.user_id==user.id).order_by(AIConversation.updated_at.desc()))).all())
@router.get('/conversations/{conversation_id}',response_model=list[MessagePublic])
async def messages(conversation_id:int,db=Depends(get_db),user=Depends(get_current_user)):
    conv=await db.scalar(select(AIConversation).where(AIConversation.id==conversation_id,AIConversation.user_id==user.id))
    if not conv:raise HTTPException(404,'Conversation not found')
    return list((await db.scalars(select(AIMessage).where(AIMessage.conversation_id==conv.id).order_by(AIMessage.created_at))).all())
@router.delete('/conversations/{conversation_id}')
async def remove(conversation_id:int,db=Depends(get_db),user=Depends(get_current_user)):
    result=await db.execute(delete(AIConversation).where(AIConversation.id==conversation_id,AIConversation.user_id==user.id));await db.commit()
    if not result.rowcount:raise HTTPException(404,'Conversation not found')
    return {'message':'Conversation deleted'}
