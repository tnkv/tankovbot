import random
from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import GenericChanceEvent

absurd_events = [
    GenericChanceEvent(
        name="Хомяк", chance_percent=0.1, action=-30,
        text="💸 Ты тапал хомяка (Hamster Kombat) полгода, но листинг провалился. От стресса усохло."
    ),
    GenericChanceEvent(
        name="Лего", chance_percent=0.1, action=-25,
        text="🦶 Ты наступил на детальку LEGO в темноте. Боль такая, что втянулось."
    ),
    GenericChanceEvent(
        name="Безумно можно", chance_percent=1.0, action=15,
        text="🌕 Безумно можно быть первым... Ауууф! Волки приняли тебя за своего. Братство волков!"
    ),
    GenericChanceEvent(
        name="ИКЕА", chance_percent=1.0, action=5,
        text="🛠 Остались лишние детали от шкафа? Ты прикрутил их к себе."
    ),
    GenericChanceEvent(
        name="Пинг 999", chance_percent=1.0, action=0,
        text="🌐 Соединение разорвано. Пакет с сантиметрами завис в маршрутизаторе. Откат (без изменений)."
    ),
    GenericChanceEvent(
        name="Проклятие бабки", chance_percent=1.0, action=-18,
        text="👵 Бабка у подъезда назвала тебя наркоманом. Жесткий сглаз!"
    ),
    GenericChanceEvent(
        name="Баг Матрицы", chance_percent=0.03, 
        action=lambda u, bg: -(u.cock_length * 2), # Inverts size: +50 -> -50
        text="💻 Ошибка в коде. Разработчик забыл поставить abs(). Твой размер вывернуло наизнанку!"
    ),
    GenericChanceEvent(
        name="Блат от Разраба", chance_percent=0.001, action=100,
        text="👑 Сам создатель бота спустился с небес и поцеловал тебя в лобик. Благословение по блату!"
    ),
    GenericChanceEvent(
        name="Апчхи", chance_percent=1.0, action=-12,
        text="💨 Ты чихнул так сильно, что случайно оторвал кусок. Зато нос дышит."
    ),
    GenericChanceEvent(
        name="Мытищи", chance_percent=1.0, action=8,
        text="🚰 Хлебнул живой водицы из-под крана в регионах. Светился ночью, зато вырос."
    ),
    GenericChanceEvent(
        name="Евангелион", chance_percent=1.0, action=-10,
        text="📺 Ты пересмотрел Еву. Твоя психика и кок разрушены. Полезай в гребаного робота, Синдзи."
    ),
    GenericChanceEvent(
        name="Качалка", chance_percent=1.0, action=15,
        text="🏋️‍♂️ Сегодня был день ног, но накачалась третья! Чистые мышцы!"
    ),
    GenericChanceEvent(
        name="Touch Grass", chance_percent=0.1, action=20,
        text="🌿 Ты наконец-то вышел на улицу и потрогал траву. Природа исцелила твою ауру."
    ),
    GenericChanceEvent(
        name="Сбербанк", chance_percent=0.1, action=-20,
        text="💳 Алло, служба безопасности. С вашего кока зафиксирован подозрительный перевод. Списание!"
    ),
    GenericChanceEvent(
        name="Школьная доска", chance_percent=0.1, action=25,
        text="🚌 Неожиданный стояк прямо у доски! Спрятать не выйдет. Чистый позор!"
    ),
    GenericChanceEvent(
        name="Дрогнула рука", chance_percent=1.0, action=-14,
        text="🩸 Решил побрить джунгли, но опасная бритва соскользнула... Зовите скорую!"
    ),
    GenericChanceEvent(
        name="Некроз", chance_percent=1.0, action=-5,
        text="⚙️ Эрекционное кольцо застряло! Некроз тканей!"
    )
]
