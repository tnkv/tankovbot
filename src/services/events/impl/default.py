from typing import Tuple, Union
from datetime import datetime
import random
from src.database.models import User
from src.services.events.base import GameEvent

class DefaultEvent(GameEvent):
    name = "Обычный день"
    description = "Ничего необычного не произошло."
    priority = 0

    def check_condition(self, user: User, current_time: datetime) -> bool:
        return True

    def apply(self, user: User, base_growth: int) -> Tuple[Union[int, str], str]:
        chance = random.randint(0, 100)
        
        # Logic for falling off (otval)
        if user.cock_length >= 100 and random.randint(0, 100) <= (user.cock_length / 100):
            return "otval", "💥 О нет! Ваш агрегат не выдержал собственного веса и отвалился..."
        
        if 0 <= chance <= 10 and user.cock_length >= -1000:
            return base_growth * -1, "📉 Упс, сегодня он немного съежился..."
        elif 10 < chance <= 95:
            return base_growth, "✨ Обычный стабильный рост."
        else:
            return "x2", "🌟 ВЕЛИКАЯ УДАЧА! Ваш размер удвоился!"
