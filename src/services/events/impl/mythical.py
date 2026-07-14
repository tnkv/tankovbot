import random
from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import GenericChanceEvent

mythical_events = [
    GenericChanceEvent(
        name="Укус паука", chance_percent=0.3, action=35,
        text="🕸 Радиоактивный паук укусил прямо в него! Теперь он пускает паутину и вырос на +35 см!"
    ),
    GenericChanceEvent(
        name="Передоз", chance_percent=0.05, action=80,
        text="🚑 Ты сожрал пачку Виагры. В глазах синеет, но +80 см! (Жди беды завтра...)"
    ),
    GenericChanceEvent(
        name="Зелье", chance_percent=0.2, 
        action=lambda u, bg: random.randint(-40, 40),
        text="🧪 Дед-травник дал отвар из сушеных жаб. Эффект непредсказуем!"
    ),
    GenericChanceEvent(
        name="Сила Земли", chance_percent=0.7, action=22,
        text="🥒 Съел генно-модифицированный огурец не отрывая от ботвы. Сила земли дала тебе +22 см."
    ),
    GenericChanceEvent(
        name="Парадокс", chance_percent=0.1, 
        action=lambda u, bg: -(u.cock_length // 2) if u.cock_length > 0 else 0, # "Откат на 3 дня", we'll just halve it
        text="🕰 Пространственно-временной континуум порвался. Твой размер откатился в прошлое (деление на 2)."
    ),
    GenericChanceEvent(
        name="Двойник", chance_percent=0.1, 
        action=lambda u, bg: -(u.cock_length * 2), # full inversion
        text="🌌 Злой двойник с бородкой из параллельной вселенной поменялся с тобой местами! Инверсия!"
    ),
    GenericChanceEvent(
        name="Галоперидол", chance_percent=0.1, action="otval",
        text="🏥 Доктор заставил принять таблетки от шизы. Оказалось, твой гигантский кок был галлюцинацией. Размер 0."
    ),
    GenericChanceEvent(
        name="Лапа обезьяны", chance_percent=0.1, action=50,
        text="👺 Ты загадал желание проклятому артефакту. +50 см, но какой ценой..."
    ),
    GenericChanceEvent(
        name="Наномашины", chance_percent=0.15, action=45,
        text="👔 Твердеют в ответ на физическую травму! Сенатор Армстронг дарует тебе +45 см!"
    ),
    GenericChanceEvent(
        name="Алхимия", chance_percent=0.8, action=20,
        text="🦾 Закон равноценного обмена. +20 см, но ты потерял руку и брата (шутка, просто +20)."
    ),
    GenericChanceEvent(
        name="Укус Вампира", chance_percent=1.5, action=15,
        text="🦇 Граф Дракула высосал кровь... оттуда. Набухло на +15 см вампирской мощи."
    ),
    GenericChanceEvent(
        name="Вирус", chance_percent=0.1, action=30, # text says otval then +30. We just do +30.
        text="🧠 Твой агрегат отгнил и отвалился... Но он вернется из мертвых зомби-болтом! Установлен размер 30."
    ),
    GenericChanceEvent(
        name="Зонд", chance_percent=0.6, action=25,
        text="👽 Инопланетяне перепутали отверстия, но стимуляция дала неожиданные +25 см."
    ),
    GenericChanceEvent(
        name="Чудо", chance_percent=0.02, action=77,
        text="👼 Разверзлись небеса, и ангельский хор воспел твой фаллос! Освящено на +77 см!"
    ),
    GenericChanceEvent(
        name="Контракт", chance_percent=0.05, action=66,
        text="📜 Ты продал душу Дьяволу за размер. Распишись кровью, получай свои +66 см."
    ),
    GenericChanceEvent(
        name="Уменьшитель", chance_percent=0.1, 
        action=lambda u, bg: -(u.cock_length * 2 // 3) if u.cock_length > 0 else 0, # division by 3. subtract 2/3
        text="🔬 Безумный ученый выстрелил в тебя из уменьшающего луча. Твой малыш скукожился в 3 раза."
    ),
    GenericChanceEvent(
        name="Помпа", chance_percent=0.1, action="otval",
        text="🎈 Ты слишком увлекся китайской вакуумной помпой. БАБАХ! И ничего не осталось (0 см)."
    ),
    GenericChanceEvent(
        name="Пила", chance_percent=0.4, action=-30,
        text="🤡 Я хочу сыграть с тобой в игру... Либо ты отрезаешь 30 см, либо... А, ты уже. -30 см."
    ),
    GenericChanceEvent(
        name="Шредингер", chance_percent=0.2, 
        action=lambda u, bg: random.randint(-50, 50),
        text="📦 Твой кок в коробке Шредингера. Он одновременно вырос и отвалился. Случайное изменение."
    ),
    GenericChanceEvent(
        name="Третий Удар", chance_percent=0.01, action=100,
        text="✝️ ТУМБЛИНГ ДАУН... Произошел Конец Света. Все превратились в лужицу LCL, а ты стал богом нового мира с +100 см!"
    )
]
