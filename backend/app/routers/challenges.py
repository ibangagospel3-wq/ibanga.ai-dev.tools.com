from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import get_current_user
from app.models.challenge import Challenge
from app.models.submission import Submission
from app.models.user import User
from app.schemas.challenge import ChallengePublic,SubmissionCreate,SubmissionResult
router=APIRouter(prefix='/api/challenges',tags=['Challenges'])
@router.get('',response_model=list[ChallengePublic])
async def all_challenges(db:AsyncSession=Depends(get_db)):return list((await db.scalars(select(Challenge).order_by(Challenge.id))).all())
@router.get('/{challenge_id}',response_model=ChallengePublic)
async def get_challenge(challenge_id:int,db:AsyncSession=Depends(get_db)):
    item=await db.get(Challenge,challenge_id)
    if not item:raise HTTPException(404,'Challenge not found')
    return item
@router.post('/{challenge_id}/submit',response_model=SubmissionResult)
async def submit(challenge_id:int,payload:SubmissionCreate,db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):
    item=await db.get(Challenge,challenge_id)
    if not item:raise HTTPException(404,'Challenge not found')
    text=' '.join([payload.html_code,payload.css_code,payload.javascript_code]).lower();expected=item.expected_behavior.lower()
    passed=all(token in text for token in expected.split() if len(token)>2)
    db.add(Submission(user_id=user.id,challenge_id=challenge_id,**payload.model_dump(),passed=passed));await db.commit()
    return {'passed':passed,'message':'Challenge completed successfully' if passed else 'Try again and check the expected behavior.'}
