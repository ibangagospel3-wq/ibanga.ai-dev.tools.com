from app.services.project_service import get_project

def test_project_service_exists():
    assert callable(get_project)
