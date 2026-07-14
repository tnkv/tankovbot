import random
from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import GenericChanceEvent

absurd_events = [
    GenericChanceEvent(
        name="Хомяк", chance_percent=0.4, action=-30,
        text="💸 Ты тапал хомяка (Hamster Kombat) полгода, но листинг провалился. От стресса усохло на 30 см."
    ),
    GenericChanceEvent(
        name="Лего", chance_percent=0.6, action=-25,
        text="🦶 Ты наступил на детальку LEGO в темноте. Боль такая, что втянулось -25 см."
    ),
    GenericChanceEvent(
        name="Безумно можно", chance_percent=1.5, action=15,
        text="🌕 Безумно можно быть первым... Ауууф! Волки приняли тебя за своего. +15 см за братство."
    ),
    GenericChanceEvent(
        name="ИКЕА", chance_percent=4.0, action=5,
        text="🛠 Остались лишние детали от шкафа? Ты прикрутил их к себе. +5 см!"
    ),
    GenericChanceEvent(
        name="Пинг 999", chance_percent=1.0, action=0,
        text="🌐 Соединение разорвано. Пакет с сантиметрами завис в маршрутизаторе. Откат (без изменений)."
    ),
    GenericChanceEvent(
        name="Проклятие бабки", chance_percent=1.0, action=-18,
        text="👵 Бабка у подъезда назвала тебя наркоманом. Жесткий сглаз на -18 см!"
    ),
    GenericChanceEvent(
        name="Баг Матрицы", chance_percent=0.1, 
        action=lambda u, bg: -(u.cock_length * 2), # Inverts size: +50 -> -50
        text="💻 Ошибка в коде. Разработчик забыл поставить abs(). Твой размер вывернуло наизнанку!"
    ),
    GenericChanceEvent(
        name="Блат от Разраба", chance_percent=0.01, action=100,
        text="👑 Сам создатель бота спустился с небес и поцеловал тебя в лобик. +100 см по блату!"
    ),
    GenericChanceEvent(
        name="Казино", chance_percent=0.1, 
        action=lambda u, bg: 50 if random.uniform(0, 100) <= 10 else -30,
        text="🍒 Все на красное! Иии... [Джекпот +50! / Ты проиграл квартиру и -30 см]."
    ),
    GenericChanceEvent(
        name="Гача", chance_percent=3.0, 
        action=lambda u, bg: 50 if random.uniform(0, 100) <= 3.33 else (10 if random.uniform(0, 100) <= 30 else 3), # simplified chances
        text="🌠 Желтая комета! Ты крутанул гачу и выбил [Мусор / Эпик / Легу]."
    ),
    GenericChanceEvent(
        name="Апчхи", chance_percent=2.0, action=-12,
        text="💨 Ты чихнул так сильно, что случайно оторвал кусок. -12 см, зато нос дышит."
    ),
    GenericChanceEvent(
        name="Мытищи", chance_percent=3.0, action=8,
        text="🚰 Хлебнул живой водицы из-под крана в регионах. Светился ночью, зато +8 см."
    ),
    GenericChanceEvent(
        name="Евангелион", chance_percent=3.0, action=-10,
        text="📺 Ты пересмотрел Еву. Твоя психика и кок разрушены. -10 см, полезай в гребаного робота, Синдзи."
    ),
    GenericChanceEvent(
        name="Качалка", chance_percent=1.5, action=15,
        text="🏋️‍♂️ Сегодня был день ног, но накачалась третья! +15 см чистых мышц."
    ),
    GenericChanceEvent(
        name="Touch Grass", chance_percent=0.8, action=20,
        text="🌿 Ты наконец-то вышел на улицу и потрогал траву. Природа исцелила твою ауру на +20 см."
    ),
    GenericChanceEvent(
        name="Лицензия", chance_percent=0.1, action="otval",
        text="📜 Ты не глядя нажал «Принимаю», а там мелким шрифтом было про изъятие агрегата. Юридический отвал (0)."
    ),
    GenericChanceEvent(
        name="Сбербанк", chance_percent=0.8, action=-20,
        text="💳 Алло, служба безопасности. С вашего кока зафиксирован подозрительный перевод. Мы списываем 20 см."
    ),
    GenericChanceEvent(
        name="Школьная доска", chance_percent=0.6, action=25,
        text="🚌 Неожиданный стояк прямо у доски! Спрятать не выйдет. +25 см чистого позора."
    ),
    GenericChanceEvent(
        name="Дрогнула рука", chance_percent=1.5, action=-14,
        text="🩸 Решил побрить джунгли, но опасная бритва соскользнула... Минус 14 см, зовите скорую."
    ),
    GenericChanceEvent(
        name="Некроз", chance_percent=4.0, action=-5,
        text="⚙️ Эрекционное кольцо застряло! -5 см из-за некроза тканей."
    )
]
