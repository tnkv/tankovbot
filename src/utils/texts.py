from datetime import timedelta, datetime
import locale

CAN_AFTER24 = "\nВы сможете крутануть свой кок ещё раз завтра."
NOT_FOUND = "Команда или аргумент некорректны! Проверьте написание если уверены в наличии данного функционала."
START_MSG = """Бот с функцией крутануть кок ✅

Автор: @tnkv_trolling
Доступные команды:
<code>/кок</code>

<code>/кок топ</code>
<code>/кок антитоп</code>
"""

ADD_TO_CHAT = """Спасибо что добавили меня в чат!
Бот с функцией крутануть кок ✅ 
Автор: @tnkv_shitpost

Доступные команды:
<code>/кок</code>
<code>/кок топ</code>
<code>/кок антитоп</code>

⚠️ Для того чтобы бот мог удалять команды пользователя во время кулдауна, необходимо выдать права администратора. ⚠️
Для этого требуется только право на удаление сообщений. 
"""

ACCESS_DENIED = "Использование этой команды от лица данного пользователя невозможно. Пользователь находится в списке заблокированных."

def wait_msg(time_seconds: int) -> str:
    t = timedelta(seconds=int(time_seconds))
    return f"😐 Вы не можете крутануть свой кок, с момента последней прокрутки прошло менее 24х часов.\n✅ Осталось: {t}"

def profile_msg(db_reg_date: int, db_cock_length: int, db_last_cock: int, db_old_cock: int) -> str:
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    except Exception:
        pass
    
    # Adding 3 hours for MSK timezone explicitly as it was in original code
    reg_date_str = f"{datetime.utcfromtimestamp(db_reg_date + (3600 * 3)).strftime('%d %b. %Y г., %H:%M')} МСК"
    last_cock_str = f"{datetime.utcfromtimestamp(db_last_cock + (3600 * 3)).strftime('%d %b. %Y г., %H:%M')} МСК"
    
    return f"""✅ Длина вашего кока: {db_cock_length} см.
🚀 Максимально отпавший кок: {db_old_cock}
💀 Дата последнего кручения: {last_cock_str}
🤓 Дата регистрации: {reg_date_str}"""

def cock_msg(action: str, num: int = 0, now_cock: int = 0) -> str:
    if action == "otval":
        return f"🤯 | Ваш кок оторвался и улетел вдаль, пиздец...\nЕго длина была равна: {num} см.{CAN_AFTER24}"
    elif action == "x2":
        return f"😎 | Ваш кок увеличился в два раза!\nТеперь его длина равна: {now_cock} см.{CAN_AFTER24}"
    elif action == "+":
        return f"➕ | Ваш кок увеличился на {num} см.\nТеперь его длина: {now_cock} см.{CAN_AFTER24}"
    else:
        return f"➖ | Ваш кок уменьшился на {num} см.\nТеперь его длина: {now_cock} см.{CAN_AFTER24}"
