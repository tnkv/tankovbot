from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import ConditionEvent

catchup_events = [
    ConditionEvent(
        name="Целочисленное переполнение",
        condition=lambda u, dt: u.cock_length < -500,
        chance_percent=10.0,
        action=lambda u, bg: -u.cock_length + 500,
        text="💻 Критический баг Вселенной: значение твоего кока ушло так глубоко в минус, что пробило дно памяти и обнулилось с другой стороны! Движок выдал тебе +500 см!",
        priority=100
    ),
    ConditionEvent(
        name="Исекай (Перерождение)",
        condition=lambda u, dt: u.cock_length < -800,
        chance_percent=30.0,
        action=lambda u, bg: -u.cock_length,
        text="🚛 Грузовик-сан сбил твой микро-кок... Он переродился в фэнтези-мире! Сегодня размер 0, но завтра он вернется с силой Избранного Героя.",
        priority=99
    ),
    ConditionEvent(
        name="Гномы-шахтеры",
        condition=lambda u, dt: u.cock_length < -300,
        chance_percent=15.0,
        action=300,
        text="💎 ROCK AND STONE! Гномы копали глубоко в шахте и случайно наткнулись на твой ствол. Откопали на +300 см!",
        priority=98
    ),
    ConditionEvent(
        name="Эффект Рогатки",
        condition=lambda u, dt: u.cock_length < -200,
        chance_percent=15.0,
        action=lambda u, bg: (abs(u.cock_length) * 2) + 20,
        text="🏹 Чем сильнее оттягиваешь резинку, тем мощнее выстрел! Твоя гигантская впадина выстрелила наружу с бешеной скоростью! Полная инверсия и +20 см сверху!",
        priority=97
    ),
    ConditionEvent(
        name="Автосервис у Ашота",
        condition=lambda u, dt: u.cock_length < -150,
        chance_percent=10.0,
        action=150,
        text="🛠️ Ты заехал на эстакаду, и мужики поддомкратили твою вмятину пневматикой. Нехилый буст на +150 см, с тебя бутылка!",
        priority=96
    ),
    ConditionEvent(
        name="Белая Дыра",
        condition=lambda u, dt: u.cock_length < -100,
        chance_percent=8.0,
        action=lambda u, bg: abs(u.cock_length) * 2,
        text="🌌 Твой минус стал настолько плотным, что сколлапсировал, превратился в Белую Дыру и выплюнул материю обратно! Математический модуль превратил минус в плюс!",
        priority=95
    ),
    ConditionEvent(
        name="Спасательная операция МЧС",
        condition=lambda u, dt: u.cock_length < -50,
        chance_percent=20.0,
        action=lambda u, bg: -u.cock_length + 15,
        text="🚁 Соседи вызвали спасателей, услышав твой плач. МЧС пригнали лебедку, зацепили то, что осталось, и вытянули наружу. Теперь у тебя стабильные +15 см. Больше не болей.",
        priority=94
    )
]
