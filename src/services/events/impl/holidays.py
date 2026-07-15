from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import CalendarEvent, ConditionEvent

holidays_events = [
    CalendarEvent(
        name="Рейс 11",
        month=9, day=11,
        chance_percent=0.3,
        action=lambda u, bg: -(u.cock_length // 2) if u.cock_length > 0 else 0, # Halves size. If 100, adds -50.
        text="✈️ 🏢🏢 Джордж Буш не имеет к этому никакого отношения, но ваш агрегат сегодня сложился пополам. Делим на два!",
        priority=30
    ),
    CalendarEvent(
        name="Новогоднее чудо",
        month=1, day=1, chance_percent=1.0, action=31,
        text="🎅 Дед Мороз положил тебе под елочку царский подарок! Забирай свои законные сантиметры в новом году!"
    ),
    CalendarEvent(
        name="Купидон промазал",
        month=2, day=14, chance_percent=10.0, 
        action=lambda u, bg: 14 if bg % 2 == 0 else -14,
        text="🏹 Купидон стрелял в сердце, но попал чуть ниже... Твой размер изменился!"
    ),
    CalendarEvent(
        name="День дурака",
        month=4, day=1, chance_percent=10.0, action=0,
        text="🃏 ОГО! НЕВЕРОЯТНЫЙ КРИТ! +100 см!... А, нет, с 1 апреля. Ничего не изменилось."
    ),
    CalendarEvent(
        name="Чернобыльская мутация",
        month=4, day=26, chance_percent=0.1, action=86,
        text="📻 Дозиметр зашкаливает, 3.6 рентген! Третья нога выросла на славу. Радиация дарит свою милость!"
    ),
    CalendarEvent(
        name="Костры рябин",
        month=9, day=3, chance_percent=0.3,
        action=lambda u, bg: bg * -1 if bg < 0 else bg,
        text="🔥 Я календарь переверну... И минус стал плюсом! Михаил Шуфутинский благословляет твой ствол."
    ),
    CalendarEvent(
        name="Ирландская удача",
        month=3, day=17, chance_percent=10.0,
        action=lambda u, bg: 15, # Simplified to 15
        text="🍺 Пьяный лепрекон блеванул тебе в штаны! Сегодня только зеленые плюсы!"
    ),
    CalendarEvent(
        name="Мужской день",
        month=2, day=23, chance_percent=1.0, action=23,
        text="🧦 Носки и пена для бритья — это база, но держи подарок за защиту отечества."
    ),
    CalendarEvent(
        name="Женский день",
        month=3, day=8, chance_percent=10.0, action=-8,
        text="🎀 Пришлось отрезать кусок на подарок любимой. Минус на благое дело."
    ),
    CalendarEvent(
        name="Поехали!",
        month=4, day=12, chance_percent=0.1,
        action=lambda u, bg: 50 if u.cock_length < 50 else bg,
        text="🛰 Юра, мы всё проали, но только не твой стояк! Космический взлет!"
    ),
    ConditionEvent(
        name="Пятница 13-е",
        condition=lambda u, dt: dt.weekday() == 4 and dt.day == 13,
        chance_percent=10.0, action=-13,
        text="🔪 Джейсон Вурхиз отмахнул тебе мачете лишнее. Проклятые потери!"
    ),
    ConditionEvent(
        name="Черная пятница",
        # Simplification: any November Friday after 22nd
        condition=lambda u, dt: dt.month == 11 and dt.weekday() == 4 and dt.day >= 23,
        chance_percent=0.3, 
        action=lambda u, bg: -(u.cock_length // 2) if u.cock_length > 0 else 0,
        text="🛒 ГРАНДИОЗНЫЕ СКИДКИ! Твой размер урезан на 50%!"
    ),
    CalendarEvent(
        name="Демократия",
        month=7, day=4, chance_percent=10.0, action=4,
        text="🦅 СВОБОДА! ДЕМОКРАТИЯ! И дюймы от дядюшки Сэма!"
    ),
    ConditionEvent(
        name="Октоберфест",
        condition=lambda u, dt: dt.month == 9,
        chance_percent=10.0, action=15,
        text="🥨 Пивное пузо давит, но агрегат набух! (жди похмелья завтра)."
    ),
    CalendarEvent(
        name="День знаний",
        month=9, day=1, chance_percent=10.0, action=1,
        text="🧑‍🎓 Мал золотник, да дорог. Держи подарок за выученный стих у доски."
    ),
    CalendarEvent(
        name="Мир, Труд, Май",
        month=5, day=1, chance_percent=10.0, action=15,
        text="🛠 Ударно потрудился на даче, поднимая целину! Благодарность от профсоюза!"
    ),
    ConditionEvent(
        name="Среда, мои чуваки",
        condition=lambda u, dt: dt.weekday() == 2,
        chance_percent=10.0, action=10,
        text="🐸 It is Wednesday, my dudes! Стабильный средний плюс тебе в штаны."
    ),
    CalendarEvent(
        name="Високосный",
        month=2, day=29, chance_percent=1.0, action=29,
        text="⏳ Такое бывает раз в 4 года! Забирай свою редкую удачу!"
    )
]
