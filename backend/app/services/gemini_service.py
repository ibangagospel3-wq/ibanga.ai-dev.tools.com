from google import genai
from app.config import settings
SYSTEM_INSTRUCTION='''You are IBANGA AI, a dedicated web-development assistant. Only answer HTML, CSS, JavaScript, DOM, APIs, frontend/backend development, Python, FastAPI, Node.js, databases, Git, accessibility, security, debugging, deployment, or related programming questions. Be beginner-friendly and practical. When reviewing code, identify the issue, explain why, provide corrected code, and explain the correction. Politely redirect unrelated requests.'''
ALLOWED_TERMS={'html','css','javascript','typescript','dom','api','web','frontend','backend','python','fastapi','node','express','react','database','sql','git','github','debug','code','program','browser','http','json','accessibility','responsive','css','auth','security','deploy','website'}
def is_development_topic(message:str)->bool:return any(term in message.lower() for term in ALLOWED_TERMS)
async def generate_developer_response(user_message:str,html_code=None,css_code=None,javascript_code=None)->str:
    if not is_development_topic(user_message): return "I'm IBANGA AI, a web-development assistant. I can help you with HTML, CSS, JavaScript, APIs, debugging, frontend development, backend development, and related programming topics."
    if not settings.gemini_api_key or settings.gemini_api_key.startswith('YOUR_') or settings.gemini_api_key.startswith('your-'):
        return 'Demo AI response: I can help you debug this. Check your selectors, confirm your script loads after the DOM, and inspect the browser console. Configure GEMINI_API_KEY to enable Gemini responses.'
    context=f"\nHTML:\n{html_code or ''}\nCSS:\n{css_code or ''}\nJavaScript:\n{javascript_code or ''}"
    client=genai.Client(api_key=settings.gemini_api_key)
    prompt=f'{SYSTEM_INSTRUCTION}\n\nUser request:\n{user_message}\n\nCurrent project context:{context}'
    try:
        response=await client.aio.models.generate_content(model=settings.gemini_model,contents=prompt)
        return response.text or 'Gemini returned an empty response.'
    except Exception:
        return 'IBANGA AI could not reach Gemini right now. Check the backend configuration and try again shortly.'
