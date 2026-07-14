from src.database.models import User
from src.services.formatting import format_top_message

def test_format_top_message():
    users = [
        User(tgid="1", username="testuser", first_name="Test", last_name="User", cock_length=150, old_cock=0),
        User(tgid="2", username=None, first_name="NoName", last_name=None, cock_length=120, old_cock=0),
        User(tgid="3", username="third", first_name="Third", last_name=None, cock_length=0, old_cock=200) # Length 0
    ]
    
    # Test top
    msg = format_top_message(users, "top")
    assert "🏆 Топ коков" in msg
    assert "testuser" in msg
    assert "Test User" in msg
    assert "150 см" in msg
    assert "NoName" in msg
    assert "120 см" in msg
    # User 3 should be skipped in normal top because value is 0 (or it was length 0)
    assert "Third" not in msg

    # Test lngst
    msg = format_top_message(users, "lngst")
    assert "🏆 Топ оторвавшихся коков" in msg
    # In lngst, user 1 and 2 have old_cock = 0, so they are skipped.
    assert "Third" in msg
    assert "200 см" in msg
    assert "Test User" not in msg
