from typing import Sequence
from src.database.models import User
from src.utils.texts import pluralize_days

def format_top_message(users: Sequence[User], stts: str) -> str:
    if stts == "top": 
        msg = "<b>🏆 Топ коков</b>"
    elif stts == "atop": 
        msg = "<b>🏆 Анти-Топ коков</b>"
    elif stts == "lngst": 
        msg = "<b>🏆 Топ оторвавшихся коков</b>"
    elif stts == "truet": 
        msg = "<b>🏆 Топ коков за 2 недели</b>"
    elif stts == "streak":
        msg = "<b>🏆 Топ стояков</b>"
    else: 
        msg = "<b>trolling</b>"
        
    for i, user in enumerate(users, start=1):
        if stts == "lngst":
            value = user.old_cock
            value_str = f"{value} см."
        elif stts == "streak":
            value = user.streak
            value_str = f"стояк {pluralize_days(value)}"
        else:
            value = user.cock_length
            value_str = f"{value} см."
            
        if value <= 0:
            continue
            
        if user.username and user.username != "None":
            msg += f'\n{i}) <a href="t.me/{user.username}">{user.full_name}</a>: {value_str}'
        else:
            msg += f"\n{i}) <code>{user.tgid}</code>: {user.full_name} - {value_str}"
            
    return msg
