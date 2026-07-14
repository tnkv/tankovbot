import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock

from src.database.models import User
from src.services.events.base import GameEvent
from src.services.events.registry import EventRegistry
from src.services.events.templates import GenericChanceEvent, CalendarEvent, ConditionEvent

# We need to import all events to test them all
from src.services.game import event_registry

class DummyEvent(GameEvent):
    def __init__(self, priority=10):
        self.priority = priority
    def check_condition(self, user, current_time):
        return True
    def apply(self, user, base_growth):
        return 1, "test"

def test_event_registry_sorting():
    registry = EventRegistry()
    e1 = DummyEvent(priority=10)
    e2 = DummyEvent(priority=50)
    e3 = DummyEvent(priority=5)
    
    registry.register(e1)
    registry.register(e2)
    registry.register(e3)
    
    assert registry._events[0].priority == 50
    assert registry._events[1].priority == 10
    assert registry._events[2].priority == 5

def test_event_registry_highest_priority():
    registry = EventRegistry()
    
    e_high = DummyEvent(priority=100)
    e_high.check_condition = lambda u, dt: False # won't trigger
    
    e_mid = DummyEvent(priority=50)
    e_mid.check_condition = lambda u, dt: True # will trigger
    
    e_low = DummyEvent(priority=10)
    e_low.check_condition = lambda u, dt: True # would trigger, but priority lower
    
    registry.register(e_low)
    registry.register(e_high)
    registry.register(e_mid)
    
    winner = registry.get_highest_priority_event(User(tgid="1", cock_length=0), datetime.now())
    assert winner == e_mid

def test_generic_chance_event():
    event = GenericChanceEvent("Test", chance_percent=50.0, action=10, text="Test event")
    user = User(tgid="1", cock_length=10)
    
    with patch('src.services.events.templates.random.uniform') as mock_uniform:
        mock_uniform.return_value = 49.0
        assert event.check_condition(user, datetime.now()) == True
        
        mock_uniform.return_value = 51.0
        assert event.check_condition(user, datetime.now()) == False
        
    action, text = event.apply(user, base_growth=5)
    assert action == 10
    assert text == "Test event"

def test_calendar_event():
    event = CalendarEvent("Test Holiday", month=12, day=31, chance_percent=100.0, action="x2", text="Happy New Year")
    user = User(tgid="1", cock_length=10)
    
    dt_match = datetime(2023, 12, 31)
    dt_miss = datetime(2023, 12, 30)
    
    with patch('src.services.events.templates.random.uniform') as mock_uniform:
        mock_uniform.return_value = 0.0
        assert event.check_condition(user, dt_match) == True
        assert event.check_condition(user, dt_miss) == False
        
    action, text = event.apply(user, base_growth=5)
    assert action == "x2"

def test_condition_event():
    event = ConditionEvent(
        "Size Test", 
        condition=lambda u, dt: u.cock_length > 100, 
        chance_percent=100.0, 
        action=lambda u, bg: u.cock_length * 2, 
        text="Big"
    )
    u_small = User(tgid="1", cock_length=50)
    u_big = User(tgid="2", cock_length=150)
    
    with patch('src.services.events.templates.random.uniform') as mock_uniform:
        mock_uniform.return_value = 0.0
        assert event.check_condition(u_small, datetime.now()) == False
        assert event.check_condition(u_big, datetime.now()) == True
        
    action, text = event.apply(u_big, base_growth=10)
    assert action == 300 # 150 * 2

def test_all_registered_events_callable():
    """
    Smoke test to ensure none of the 100+ events throw exceptions 
    when calling check_condition or apply with dummy data.
    This catches syntax errors in lambdas, wrong signatures, etc.
    """
    user_positive = User(tgid="1", cock_length=50)
    user_negative = User(tgid="2", cock_length=-500)
    user_zero = User(tgid="3", cock_length=0)
    dt = datetime(2023, 5, 10)
    
    for event in event_registry._events:
        try:
            # We don't care about the return value, just that it doesn't crash
            event.check_condition(user_positive, dt)
            event.check_condition(user_negative, dt)
            event.check_condition(user_zero, dt)
            
            event.apply(user_positive, 10)
            event.apply(user_negative, 10)
            event.apply(user_zero, 10)
        except Exception as e:
            pytest.fail(f"Event '{event.name}' raised an exception: {e}")
