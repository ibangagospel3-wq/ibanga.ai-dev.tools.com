from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

from app.main import app, frontend_origin


def test_cors_allows_production_and_local_frontend_origins():
    cors = next(
        middleware
        for middleware in app.user_middleware
        if middleware.cls is CORSMiddleware
    )
    origins = cors.kwargs['allow_origins']

    assert 'https://ibangagospel3-wq.github.io' in origins
    assert 'http://localhost:5500' in origins
    assert 'http://127.0.0.1:5500' in origins
    assert '*' not in origins
    assert cors.kwargs['allow_credentials'] is True


def test_production_preflight_returns_cors_headers():
    response = TestClient(app).options(
        '/api/auth/login',
        headers={
            'Origin': 'https://ibangagospel3-wq.github.io',
            'Access-Control-Request-Method': 'POST',
        },
    )

    assert response.status_code == 200
    assert response.headers['access-control-allow-origin'] == (
        'https://ibangagospel3-wq.github.io'
    )
    assert response.headers['access-control-allow-credentials'] == 'true'


def test_frontend_url_is_reduced_to_a_safe_origin():
    assert frontend_origin('https://example.com/repo/page?x=1') == (
        'https://example.com'
    )
    assert frontend_origin('javascript:alert(1)') is None
    assert frontend_origin('https://user:password@example.com') is None
