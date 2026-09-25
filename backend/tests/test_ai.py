from app.services.gemini_service import is_development_topic

def test_ai_topic_filter():
    assert is_development_topic('Why is my JavaScript button not working?')
    assert not is_development_topic('Who should I vote for?')
