# IBANGA AI Developers Tool Backend

FastAPI + PostgreSQL + SQLAlchemy 2.x + JWT/Argon2 + Gemini backend for the existing IBANGA frontend.

The repository root also contains VS Code settings for the frontend workspace; when opening this `backend` folder directly in VS Code, its local `.vscode/settings.json` selects `backend/.venv`.

## Requirements

- Python 3.11+
- PostgreSQL
- Gemini API key from Google AI Studio for live AI responses

## Setup on Windows

From the `backend` directory:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create a PostgreSQL database named `ibanga_ai`, then copy `.env.example` to `.env` and set `DATABASE_URL`, a long `SECRET_KEY`, and `GEMINI_API_KEY`.

The repository already contains a `.env` placeholder for local setup. Replace placeholders locally and never commit that file.

## Database

Run the migration and seed content:

```powershell
alembic upgrade head
python seed.py
```

The seed creates example HTML, CSS, and JavaScript lessons plus a beginner challenge. It does not create users or passwords.

## Run

```powershell
uvicorn app.main:app --reload
```

- API: `http://127.0.0.1:8000/api`
- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Health: `http://127.0.0.1:8000/api/health`

Serve the frontend with VS Code Live Server on port 5500. The frontend API client uses `http://127.0.0.1:8000/api` by default. To change it before loading frontend scripts, set `window.IBANGA_API_URL`.

## Authentication flow

Register with `POST /api/auth/register`, log in with `POST /api/auth/login`, and store only the returned access token on the frontend demo. Protected requests use `Authorization: Bearer <token>`. A production deployment should prefer secure HttpOnly refresh-cookie architecture and should not treat localStorage as a secure token vault.

## Gemini

`GEMINI_API_KEY` is read only by `app/services/gemini_service.py`. Without a configured key, the API returns a clearly labeled demo response. The backend filters unrelated topics before calling Gemini and rate-limits authenticated users using `AI_RATE_LIMIT_PER_MINUTE`.

Production Gemini requests follow:

`Frontend → FastAPI → Gemini`

Never place the key in frontend JavaScript, HTML, CSS, localStorage, README files, or screenshots.

## Testing

After installing dependencies:

```powershell
pytest
```

The included tests cover password policy, AI topic restriction, and service availability. Add a PostgreSQL-backed test database for full endpoint integration tests.

## Production checklist

Use HTTPS, a unique secret, a production PostgreSQL URL, restricted `FRONTEND_URL`, a reverse proxy, structured logging, a real rate-limit store such as Redis, secure refresh tokens, and server-side validation. Do not use wildcard CORS in production.

## API groups

- `/api/auth` — register, login, me, logout
- `/api/users` — current profile
- `/api/projects` — authenticated owned CRUD
- `/api/lessons` — public lesson catalog
- `/api/progress` — authenticated completion
- `/api/challenges` — catalog and protected submissions
- `/api/ai` — protected chat, code actions, and conversation history
- `/api/notifications` — protected notification list/read
- `/api` and `/api/health` — system information
