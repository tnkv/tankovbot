from abc import ABC, abstractmethod
from typing import Tuple, Union
from datetime import datetime
from src.database.models import User

class GameEvent(ABC):
    name: str
    description: str
    priority: int = 0

    @abstractmethod
    def check_condition(self, user: User, current_time: datetime) -> bool:
        """
        Check if the event should trigger based on user state or current time.
        """
        pass

    @abstractmethod
    def apply(self, user: User, base_growth: int) -> Tuple[Union[int, str], str]:
        """
        Apply the event logic. 
        Returns a tuple of (final_growth, event_text).
        final_growth can be an int (the amount to change) or string ("otval", "x2").
        """
        pass
