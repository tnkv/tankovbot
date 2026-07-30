from typing import Tuple, Union
from datetime import datetime
import random
from src.database.models import User
from src.services.events.base import GameEvent
from src.utils.texts import pluralize_days

class StreakEvent(GameEvent):
    name = "Бонус за Стояк"
    description = "Особая награда за верность и регулярный передерг."
    priority = 50

    def check_condition(self, user: User, current_time: datetime) -> bool:
        # 5% chance
        chance = random.randint(1, 100)
        return user.streak >= 10 and 1 <= chance <= 5

    def apply(self, user: User, base_growth: int) -> Tuple[Union[int, str], str]:
        streak = user.streak
        if streak < 50:
            bonus = 1
        else:
            bonus = min(10, 2 + (streak - 50) // 100)
            
        total_growth = base_growth + bonus
        msg = f"🔥 Ваша преданность поражает! За стояк в {pluralize_days(streak)} Вы получаете бонус (+{bonus} см)!"
        
        return total_growth, msg

streak_events = [StreakEvent()]
