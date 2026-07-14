from datetime import datetime
from typing import Tuple, Union
import random
from src.database.models import User
from src.services.events.registry import event_registry
from src.services.events.impl.default import DefaultEvent

from src.services.events.impl.catchup import catchup_events
from src.services.events.impl.holidays import holidays_events
from src.services.events.impl.sizes import sizes_events
from src.services.events.impl.memes import memes_events
from src.services.events.impl.absurd import absurd_events
from src.services.events.impl.mythical import mythical_events

# Register events
event_registry.register(DefaultEvent())

for e in catchup_events: event_registry.register(e)
for e in holidays_events: event_registry.register(e)
for e in sizes_events: event_registry.register(e)
for e in memes_events: event_registry.register(e)
for e in absurd_events: event_registry.register(e)
for e in mythical_events: event_registry.register(e)

def calculate_cock_growth(user: User) -> Tuple[Union[int, str], str]:
    """
    Returns a tuple of (action, event_text).
    action can be an integer (amount to add/subtract) or a string ("otval", "x2").
    """
    base_growth = random.randint(1, 20)
    current_time = datetime.now()
    
    event = event_registry.get_highest_priority_event(user, current_time)
    
    if event:
        return event.apply(user, base_growth)
    
    # Fallback just in case
    return DefaultEvent().apply(user, base_growth)
