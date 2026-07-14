from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.utils.texts import START_MSG, ADD_TO_CHAT, profile_msg
from src.database.models import User

router = Router(name="basic")

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(START_MSG)

@router.message(Command("profile", "p", "п", "профиль"))
async def profile_cmd(message: Message, user: User):
    msg = profile_msg(
        db_reg_date=user.register_date,
        db_cock_length=user.cock_length,
        db_last_cock=user.last_cock,
        db_old_cock=user.old_cock
    )
    await message.reply(msg)

@router.message(F.new_chat_members)
async def on_new_chat_members(message: Message, bot: Bot):
    if not message.new_chat_members:
        return
    bot_obj = await bot.get_me()
    for member in message.new_chat_members:
        if member.id == bot_obj.id:
            await message.answer(ADD_TO_CHAT)
