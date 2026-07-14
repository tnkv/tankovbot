import random
from typing import Tuple, Union, Callable, Optional
from datetime import datetime
from src.database.models import User
from src.services.events.base import GameEvent

class GenericChanceEvent(GameEvent):
    """
    An event that triggers purely based on a percentage chance.
    """
    def __init__(self, name: str, chance_percent: float, action: Union[int, str, Callable], text: str, priority: int = 10):
        self.name = name
        self.chance_percent = chance_percent
        self.action_val = action
        self.description = text
        self.priority = priority

    def check_condition(self, user: User, current_time: datetime) -> bool:
        return random.uniform(0, 100) <= self.chance_percent

    def apply(self, user: User, base_growth: int) -> Tuple[Union[int, str], str]:
        if callable(self.action_val):
            return self.action_val(user, base_growth), self.description
        return self.action_val, self.description

class CalendarEvent(GameEvent):
    """
    An event that triggers on a specific date (month, day) with a certain chance.
    """
    def __init__(self, name: str, month: int, day: int, chance_percent: float, action: Union[int, str, Callable], text: str, priority: int = 20):
        self.name = name
        self.month = month
        self.day = day
        self.chance_percent = chance_percent
        self.action_val = action
        self.description = text
        self.priority = priority

    def check_condition(self, user: User, current_time: datetime) -> bool:
        if current_time.month == self.month and current_time.day == self.day:
            return random.uniform(0, 100) <= self.chance_percent
        return False

    def apply(self, user: User, base_growth: int) -> Tuple[Union[int, str], str]:
        if callable(self.action_val):
            return self.action_val(user, base_growth), self.description
        return self.action_val, self.description

class ConditionEvent(GameEvent):
    """
    An event that triggers based on a condition function (checking user and/or current_time)
    and a percentage chance.
    """
    def __init__(self, name: str, condition: Callable[[User, datetime], bool], chance_percent: float, action: Union[int, str, Callable], text: str, priority: int = 15):
        self.name = name
        self.condition = condition
        self.chance_percent = chance_percent
        self.action_val = action
        self.description = text
        self.priority = priority

    def check_condition(self, user: User, current_time: datetime) -> bool:
        if self.condition(user, current_time):
            return random.uniform(0, 100) <= self.chance_percent
        return False

    def apply(self, user: User, base_growth: int) -> Tuple[Union[int, str], str]:
        if callable(self.action_val):
            return self.action_val(user, base_growth), self.description
        return self.action_val, self.description
