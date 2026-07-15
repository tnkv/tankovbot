import random
from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import GenericChanceEvent

mythical_events = [
    GenericChanceEvent(
        name="Укус паука", chance_percent=0.1, action=35,
        text="🕸 Радиоактивный паук укусил прямо в него! Теперь он пускает паутину и вырос на +35 см!"
    ),
    GenericChanceEvent(
        name="Передоз", chance_percent=0.01, action=80,
        text="🚑 Ты сожрал пачку Виагры. В глазах синеет, но +80 см! (Жди беды завтра...)"
    ),
    GenericChanceEvent(
        name="Сила Земли", chance_percent=0.1, action=22,
        text="🥒 Съел генно-модифицированный огурец не отрывая от ботвы. Сила земли дала тебе +22 см."
    ),
    GenericChanceEvent(
        name="Лапа обезьяны", chance_percent=0.01, action=50,
        text="👺 Ты загадал желание проклятому артефакту. +50 см, но какой ценой..."
    ),
    GenericChanceEvent(
        name="Наномашины", chance_percent=0.1, action=45,
        text="👔 Твердеют в ответ на физическую травму! Сенатор Армстронг дарует тебе +45 см!"
    ),
    GenericChanceEvent(
        name="Алхимия", chance_percent=0.1, action=20,
        text="🦾 Закон равноценного обмена. +20 см, но ты потерял руку и брата (шутка, просто +20)."
    ),
    GenericChanceEvent(
        name="Укус Вампира", chance_percent=1.0, action=15,
        text="🦇 Граф Дракула высосал кровь... оттуда. Набухло на +15 см вампирской мощи."
    ),
    GenericChanceEvent(
        name="Зонд", chance_percent=0.1, action=25,
        text="👽 Инопланетяне перепутали отверстия, но стимуляция дала неожиданные +25 см."
    ),
    GenericChanceEvent(
        name="Чудо", chance_percent=0.01, action=77,
        text="👼 Разверзлись небеса, и ангельский хор воспел твой фаллос! Освящено на +77 см!"
    ),
    GenericChanceEvent(
        name="Контракт", chance_percent=0.01, action=66,
        text="📜 Ты продал душу Дьяволу за размер. Распишись кровью, получай свои +66 см."
    ),
    GenericChanceEvent(
        name="Уменьшитель", chance_percent=0.03, 
        action=lambda u, bg: -(u.cock_length * 2 // 3) if u.cock_length > 0 else 0, # division by 3. subtract 2/3
        text="🔬 Безумный ученый выстрелил в тебя из уменьшающего луча. Твой малыш скукожился в 3 раза."
    ),
    GenericChanceEvent(
        name="Пила", chance_percent=0.1, action=-30,
        text="🤡 Я хочу сыграть с тобой в игру... Либо ты отрезаешь 30 см, либо... А, ты уже. -30 см."
    ),
    GenericChanceEvent(
        name="Третий Удар", chance_percent=0.001, action=100,
        text="✝️ ТУМБЛИНГ ДАУН... Произошел Конец Света. Все превратились в лужицу LCL, а ты стал богом нового мира с +100 см!"
    )
]
