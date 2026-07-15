import random
from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import GenericChanceEvent

mythical_events = [
    GenericChanceEvent(
        name="Укус паука", chance_percent=0.1, action=35,
        text="🕸 Радиоактивный паук укусил прямо в него! Теперь он пускает паутину и вырос!"
    ),
    GenericChanceEvent(
        name="Передоз", chance_percent=0.01, action=80,
        text="🚑 Ты сожрал пачку Виагры. В глазах синеет, но силы прибавилось! (Жди беды завтра...)"
    ),
    GenericChanceEvent(
        name="Сила Земли", chance_percent=0.1, action=22,
        text="🥒 Съел генно-модифицированный огурец не отрывая от ботвы. Сила земли дала тебе свою мощь."
    ),
    GenericChanceEvent(
        name="Лапа обезьяны", chance_percent=0.01, action=50,
        text="👺 Ты загадал желание проклятому артефакту. Желание исполнено, но какой ценой..."
    ),
    GenericChanceEvent(
        name="Наномашины", chance_percent=0.1, action=45,
        text="👔 Твердеют в ответ на физическую травму! Сенатор Армстронг дарует тебе свою силу!"
    ),
    GenericChanceEvent(
        name="Алхимия", chance_percent=0.1, action=20,
        text="🦾 Закон равноценного обмена. Ты получил мощь, но ты потерял руку и брата (шутка, просто мощь)."
    ),
    GenericChanceEvent(
        name="Укус Вампира", chance_percent=1.0, action=15,
        text="🦇 Граф Дракула высосал кровь... оттуда. Набухло вампирской мощью."
    ),
    GenericChanceEvent(
        name="Зонд", chance_percent=0.1, action=25,
        text="👽 Инопланетяне перепутали отверстия, но стимуляция дала неожиданный результат."
    ),
    GenericChanceEvent(
        name="Чудо", chance_percent=0.01, action=77,
        text="👼 Разверзлись небеса, и ангельский хор воспел твой фаллос! Освящено!"
    ),
    GenericChanceEvent(
        name="Контракт", chance_percent=0.01, action=66,
        text="📜 Ты продал душу Дьяволу за размер. Распишись кровью, получай свою долю."
    ),
    GenericChanceEvent(
        name="Уменьшитель", chance_percent=0.03, 
        action=lambda u, bg: -(u.cock_length * 2 // 3) if u.cock_length > 0 else 0, # division by 3. subtract 2/3
        text="🔬 Безумный ученый выстрелил в тебя из уменьшающего луча. Твой малыш скукожился в 3 раза."
    ),
    GenericChanceEvent(
        name="Пила", chance_percent=0.1, action=-30,
        text="🤡 Я хочу сыграть с тобой в игру... Либо ты отрезаешь кусок, либо... А, ты уже."
    ),
    GenericChanceEvent(
        name="Третий Удар", chance_percent=0.001, action=100,
        text="✝️ ТУМБЛИНГ ДАУН... Произошел Конец Света. Все превратились в лужицу LCL, а ты стал богом нового мира!"
    )
]
