import random
from typing import Tuple, Union
from src.database.models import User
from src.services.events.templates import GenericChanceEvent

memes_events = [
    GenericChanceEvent(
        name="Матрица",
        chance_percent=0.5,
        action=lambda u, bg: "x2" if random.choice([True, False]) else -(u.cock_length // 2) if u.cock_length > 0 else 0,
        text="🕶 Морфеус предложил выбор. Ты глотнул таблетку и... [х2 / /2]! Добро пожаловать в реальный мир."
    ),
    GenericChanceEvent(
        name="Синий мет", chance_percent=0.05, action=99,
        text="🎩 Джесси, нам нужно варить! Чистейший продукт дал приход на +99.1 см!"
    ),
    GenericChanceEvent(
        name="Скайрим", chance_percent=0.8, action=20, # Technically we just add 20, but the text makes it look like otval + 20
        text="🏹 Тебе прострелили колено, и кок отвалился... Но эй, ты наконец-то проснулся! +20 см новой жизни."
    ),
    GenericChanceEvent(
        name="Болото Шрека", chance_percent=0.2, action=40,
        text="🟢 SOMEBODY ONCE TOLD ME... Шрек защищает твое болото! +40 см зелёной мощи."
    ),
    GenericChanceEvent(
        name="Рикролл", chance_percent=5.0, action=0,
        text="🕺 Never gonna give you up... Твой кок затанцевал и остался на месте (+0 см)."
    ),
    GenericChanceEvent(
        name="Not Stonks", chance_percent=1.5, action=-15,
        text="📉 Акции твоего стояка резко обвалились на бирже мемов. -15 см. Not Stonks."
    ),
    GenericChanceEvent(
        name="Stonks", chance_percent=0.5, action=25,
        text="📈 Волк с Уолл-стрит завидует твоему росту! Актив поднялся на +25 см! Stonks."
    ),
    GenericChanceEvent(
        name="Бебра", chance_percent=3.0, action=-10,
        text="🤢 Ты смачно понюхал бебру, но она оказалась токсичной. -10 см за любопытство."
    ),
    GenericChanceEvent(
        name="ГигаЧад", chance_percent=0.1, action=50,
        text="⬛ Безупречная челюсть, стальной взгляд. Ты стал ГигаЧадом. +50 см монолитной уверенности."
    ),
    GenericChanceEvent(
        name="Думер", chance_percent=5.0, action=-5,
        text="🎧 В наушниках играет пост-панк, на улице серый дождь... Всё тлен. -5 см из-за депрессии."
    ),
    GenericChanceEvent(
        name="Литералли ми", chance_percent=2.0, action=10,
        text="🚗 Да, я не умер в конце Драйва. Ты — это Райан Гослинг. Держи зубочистку и +10 см."
    ),
    GenericChanceEvent(
        name="YOU DIED", chance_percent=0.1, action="otval",
        text="💀 YOU DIED. Твой агрегат не смог уклониться от переката босса в Dark Souls. Отвал (0 см)."
    ),
    GenericChanceEvent(
        name="JoJo Ref", chance_percent=0.8, action=20,
        text="ORA ORA ORA! 👊 Твой станд пробудился и удлинил агрегат на +20 см! (Да, это отсылка к ДжоДжо)."
    ),
    GenericChanceEvent(
        name="Киберпанк", chance_percent=0.5, 
        action=lambda u, bg: random.choice([-10, 30]),
        text="🦾 Установил имплант «Мистер Стадд», но поймал баг Т-позы. Ваш размер: случайное изменение."
    ),
    GenericChanceEvent(
        name="Сигма", chance_percent=0.4, action=30,
        text="💼 Проснулся в 4 утра, принял ледяной душ, заигнорил женщин. +30 см за сигма-гриндсет."
    ),
    GenericChanceEvent(
        name="Backrooms", chance_percent=0.1, action=-50,
        text="🚪 Твой кок провалился сквозь текстуры реальности прямо в Закулисье (Backrooms). -50 см."
    ),
    GenericChanceEvent(
        name="Amogus", chance_percent=1.5, action=-15,
        text="🔪 SUS. Среди нас предатель... И он отрезал тебе 15 см в электрической!"
    ),
    GenericChanceEvent(
        name="Рулетка", chance_percent=0.5, 
        action=lambda u, bg: 15 if random.uniform(0, 100) <= 80 else "otval",
        text="🔫 Крутим барабан... [*Щелчок* — фух, пронесло, +15 см / *БАМ* — мозги по стене, ОТВАЛ!]"
    ),
    GenericChanceEvent(
        name="Подкрадули", chance_percent=2.0, action=12,
        text="👟 Ты надел бархатные тяги. Стиль: +0. Зато какой комфорт и +12 см в штанах кефтеме!"
    ),
    GenericChanceEvent(
        name="Моя Прелесть", chance_percent=0.8, action=-20,
        text="🌋 Ты надел Кольцо Всевластья на... него. Он исчез! (-20 см), зато теперь невидимый."
    )
]
