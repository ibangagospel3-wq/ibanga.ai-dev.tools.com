from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from urllib.parse import urlsplit
from app.config import settings
from app.database import engine
from app.routers import auth,users,projects,lessons,progress,challenges,ai,notifications
app=FastAPI(title='IBANGA AI Developers Tool API',version='1.0.0',description='Backend for learning, coding, projects, and Gemini-powered web development assistance.')


def frontend_origin(value: str) -> str | None:
    try:
        parsed = urlsplit(value.strip())
        hostname = parsed.hostname
        port = parsed.port
    except ValueError:
        return None
    scheme = parsed.scheme.lower()
    if scheme not in {'http', 'https'} or not hostname:
        return None
    if parsed.username is not None or parsed.password is not None:
        return None
    hostname = hostname.lower()
    if ':' in hostname and not hostname.startswith('['):
        hostname = f'[{hostname}]'
    if port is not None and not (
        (scheme == 'https' and port == 443)
        or (scheme == 'http' and port == 80)
    ):
        hostname = f'{hostname}:{port}'
    return f'{scheme}://{hostname}'


origins = [
    'https://ibangagospel3-wq.github.io',
    'http://localhost:5500',
    'http://127.0.0.1:5500',
    'http://localhost:5501',
    'http://127.0.0.1:5501',
]
configured_origin = frontend_origin(settings.frontend_url)
if configured_origin and configured_origin not in origins:
    origins.append(configured_origin)
app.add_middleware(CORSMiddleware,allow_origins=list(dict.fromkeys(origins)),allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
for router in (auth.router,users.router,projects.router,lessons.router,progress.router,challenges.router,ai.router,notifications.router):app.include_router(router)
@app.exception_handler(SQLAlchemyError)
async def database_error_handler(request, exc):
    return JSONResponse(status_code=503, content={'detail':'Database unavailable. Start PostgreSQL and verify DATABASE_URL.'})
@app.get('/api',tags=['System'])
async def api_info():return {'name':'IBANGA AI Developers Tool API','version':'1.0.0','status':'running'}
@app.get('/api/health',tags=['System'])
async def health():
    database='disconnected'
    try:
        async with engine.connect() as connection:await connection.execute(text('SELECT 1'));database='connected'
    except Exception:pass
    return {'status':'healthy','service':'IBANGA AI Developers Tool','database':database,'ai':'configured' if settings.gemini_api_key and not settings.gemini_api_key.startswith(('YOUR_','your-')) else 'demo'}
