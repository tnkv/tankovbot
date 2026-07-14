from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import ConditionEvent

sizes_events = [
    ConditionEvent(
        name="Сингулярность",
        condition=lambda u, dt: u.cock_length <= 0,
        chance_percent=0.1, action=100,
        text="⚛️ Твой микро-кок сжался до черной дыры и взорвался Большим Взрывом! +100 см!"
    ),
    ConditionEvent(
        name="Коллапс",
        condition=lambda u, dt: u.cock_length > 300,
        chance_percent=0.5, 
        action=lambda u, bg: -u.cock_length + 50,
        text="🪐 Гигантский червь не выдержал собственной гравитации и оторвался. Осталось 50 см."
    ),
    ConditionEvent(
        name="База",
        condition=lambda u, dt: u.cock_length == 15,
        chance_percent=1.0, action="x2",
        text="⚖️ Ты достиг идеального среднего размера. За это вселенная дарует тебе х2!"
    ),
    ConditionEvent(
        name="Налоговая",
        condition=lambda u, dt: u.cock_length > 50,
        chance_percent=1.0, action=-20,
        text="📏 Пришла налоговая по понтам. Оказалось, ты мерил от ануса. Штраф -20 см."
    ),
    ConditionEvent(
        name="Второе дыхание",
        condition=lambda u, dt: u.cock_length < -50,
        chance_percent=1.0, 
        action=lambda u, bg: -u.cock_length + 10,
        text="🩹 Врачи провели сложную операцию по вытягиванию впуклого кока. Теперь у тебя стабильные 10 см."
    ),
    ConditionEvent(
        name="Призрак",
        condition=lambda u, dt: u.cock_length == 0,
        chance_percent=50.0, action=1,
        text="🌬️ Он вроде есть, но его вроде нет... Дух святой дарует тебе +1 см надежды."
    ),
    ConditionEvent(
        name="Nice",
        condition=lambda u, dt: u.cock_length == 69,
        chance_percent=69.0, action=7, # rounded 6.9
        text="😏 Nice. Держи +6.9 см для поддержания атмосферы."
    ),
    ConditionEvent(
        name="420 Blaze It",
        condition=lambda u, dt: u.cock_length == 420,
        chance_percent=10.0, 
        action=lambda u, bg: -u.cock_length + 20,
        text="💨 Ты скурил свой агрегат. Откат до 20 см, зато было весело."
    ),
    ConditionEvent(
        name="Число зверя",
        condition=lambda u, dt: u.cock_length == 666,
        chance_percent=10.0, action="otval",
        text="🔥 Сатана забрал твой болт в ад! Полный отвал (0)."
    ),
    ConditionEvent(
        name="Error 404",
        condition=lambda u, dt: u.cock_length == 404,
        chance_percent=5.0, action=0, # Random logic needs lambda
        text="🌐 Cock not found. Перезагрузка системы... Случайная аномалия!"
    ),
    ConditionEvent(
        name="Мороз",
        condition=lambda u, dt: u.cock_length < 10 and dt.month in [12, 1, 2],
        chance_percent=3.0, action=-10,
        text="🥶 Ну он просто замерз! Скукожился на -10 см."
    ),
    ConditionEvent(
        name="Центурион",
        condition=lambda u, dt: u.cock_length == 100,
        chance_percent=0.5, action=100,
        text="🏛️ Слава Риму! Твой центурион получает легион подкрепления! +100 см."
    ),
    ConditionEvent(
        name="Золотое сечение",
        condition=lambda u, dt: u.cock_length in [16, 17],
        chance_percent=10.0, action=2, # rounded 1.6
        text="✨ Фибоначчи плачет от счастья. Идеальные пропорции дают +1.6 см к эстетике."
    ),
    ConditionEvent(
        name="Перевес",
        condition=lambda u, dt: u.cock_length > 200,
        chance_percent=0.5, action=-50,
        text="🏗 Ты не смог поднять его с кровати и потянул спину. -50 см за травмоопасность."
    ),
    ConditionEvent(
        name="Эффект Пигмалиона",
        condition=lambda u, dt: 1 <= u.cock_length <= 5,
        chance_percent=1.0, action=20,
        text="🏺 Ты так долго верил в свой огрызок, что он ожил и вырос на +20 см!"
    ),
    ConditionEvent(
        name="Уроборос",
        condition=lambda u, dt: u.cock_length < -100,
        chance_percent=1.0, 
        action=lambda u, bg: abs(u.cock_length) * 2,
        text="🔄 Он втянулся так глубоко, что вышел с другой стороны! Минус меняется на плюс."
    ),
    ConditionEvent(
        name="В яблочко",
        condition=lambda u, dt: u.cock_length == 10,
        chance_percent=5.0, action=10,
        text="🎯 Идеальная десятка удваивается!"
    ),
    ConditionEvent(
        name="Агент",
        condition=lambda u, dt: u.cock_length == 7,
        chance_percent=20.0, action=7,
        text="🍸 Взболтать, но не смешивать. Агент 007 получает +7 секретных сантиметров."
    )
]
