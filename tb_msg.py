#Список воозжможных сообщений.
from datetime import datetime, timedelta
from mmap import ACCESS_DEFAULT
from termios import TIOCPKT, TIOCPKT_DATA

can_after24 = "\nВы сможете крутануть свой кок ещё раз через 24 часа."

tb_not_found = "Команда или аргумент некорректны! Проверьте написание если уверены в наличии данного функционала."
startmsg = """Бот с функцией крутануть кок ✅
\nАвтор: @tnkv_shitpost
Доступные команды:
<code>/кок</code>

<code>/кок топ</code>
<code>/кок антитоп</code>
"""

tb_add_tochat = """Спасибо что добавили меня в чат!
Бот с функцией крутануть кок ✅ 
Автор: @tnkv_shitpost

Доступные команды:
<code>/кок</code>
<code>/кок топ</code>
<code>/кок антитоп</code>

⚠️ Для того чтобы бот мог удалять команды пользователя во время кулдауна, необходимо выдать права администратора. ⚠️
Необходимо только право на удаление сообщений.
"""


tb_access_denied = "Использование этой команды от лица данного пользователя невозможно. Пользователь находится в списке заблокированных."

def wait(time):
    time = timedelta(seconds = time)
    return f"😐 Вы не можете крутануть свой кок, с момента последней прокрутки прошло менее 24х часов.\n✅ Осталось: {time}"

def profile(db_reg_date, db_cock_lenght, db_last_cock, db_old_cock):
    db_reg_date = f"{datetime.utcfromtimestamp(db_reg_date+(3600*3)).strftime('%Y-%m-%d %H:%M:%S')} МСК"
    db_last_cock = f"{datetime.utcfromtimestamp(db_last_cock+(3600*3)).strftime('%Y-%m-%d %H:%M:%S')} МСК"
    msg = f"""✅ Длина вашего кока: {db_cock_lenght} см.
🚀 Максимально отпавший кок: {db_old_cock}
💀 Дата последнего кручения: {db_last_cock}
🤓 Дата регистрации: {db_reg_date}"""
    return msg

def tb_indev(command: str):
    return f"""Команда "<code>{command}</code>" находится в разработке, или отключена."""

def cockmsg(deystv: str, num = 0, nowcock = 0):
    if deystv == "otval":
        return "🤯 | Ваш кок оторвался и улетел вдаль, пиздец...\nЕго длина была равна: " + str(num) + " см." + can_after24
    elif deystv == "x2":
        return "😎 | Ваш кок увеличился в два раза!\nТеперь его длина равна: " + str(num) + " см." + can_after24
    elif deystv == "+":
        return "➕ | Ваш кок увеличился на " + str(num)+ " см.\nТеперь его длина: " + str(nowcock) + " см." + can_after24
    else:
        return "➖ | Ваш кок уменьшился на " + str(num)+ " см.\nТеперь его длина: " + str(nowcock) + " см." + can_after24

def cocktops(top,stts):
    if stts == "top":
        msg = "<b>🏆 Топ коков</b>"
    else:
        msg = "<b>🏆 Анти-Топ коков</b>"
    for i in top:
        if top[i][-1] == "ID":
            msg += f"\n{i}) <code>{top[i][0]}</code>: {top[i][1]} см."
        elif top[i][-1] == "FULLNAME":
            msg += f"\n{i}) <code>{top[i][0]}</code>: {top[i][1]} см."
        elif top[i][-1] == "USERNAME":
            msg += f'\n{i}) <a href="t.me/{top[i][0]}">{top[i][0]}</a>: {top[i][1]} см.'
        else:
            msg += f'\n{i}) <a href="t.me/{top[i][0]}">{top[i][1]}</a>: {top[i][2]} см.'
    return msg
