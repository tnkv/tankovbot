from typing import List, Type
from datetime import datetime
from src.database.models import User
from src.services.events.base import GameEvent

class EventRegistry:
    def __init__(self):
        self._events: List[GameEvent] = []

    def register(self, event: GameEvent):
        self._events.append(event)
        # Sort by priority descending
        self._events.sort(key=lambda e: e.priority, reverse=True)

    def get_active_events(self, user: User, current_time: datetime) -> List[GameEvent]:
        active_events = []
        for event in self._events:
            if event.check_condition(user, current_time):
                active_events.append(event)
        return active_events

    def get_highest_priority_event(self, user: User, current_time: datetime) -> GameEvent | None:
        events = self.get_active_events(user, current_time)
        return events[0] if events else None

event_registry = EventRegistry()
