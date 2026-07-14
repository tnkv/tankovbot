from typing import Sequence
from src.database.models import User

def format_top_message(users: Sequence[User], stts: str) -> str:
    if stts == "top": 
        msg = "<b>🏆 Топ коков</b>"
    elif stts == "atop": 
        msg = "<b>🏆 Анти-Топ коков</b>"
    elif stts == "lngst": 
        msg = "<b>🏆 Топ оторвавшихся коков</b>"
    elif stts == "truet": 
        msg = "<b>🏆 Топ коков за 2 недели</b>"
    else: 
        msg = "<b>trolling</b>"
        
    for i, user in enumerate(users, start=1):
        value = user.old_cock if stts == "lngst" else user.cock_length
        if value == 0:
            continue
            
        if user.username and user.username != "None":
            msg += f'\n{i}) <a href="t.me/{user.username}">{user.full_name}</a>: {value} см.'
        else:
            msg += f"\n{i}) <code>{user.tgid}</code>: {user.full_name} - {value} см."
            
    return msg
