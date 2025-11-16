from config import *
from tb_msg import *

from aiogram import Bot, Dispatcher, executor, types
from random import randint, choices
from datetime import date, datetime
from time import time

import sqlite3 as sq
import asyncio
import logging

conn = sq.connect('users.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tgusers
              (tgid TEXT, register_date INTEGER, cock_lenght INTEGER, last_cock INTEGER, old_cock INTEGER, first_name TEXT, last_name TEXT, username TEXT)''')
              # tgid -- ТГ айди пользователя
              #register_date -- Дата регистрации
              #cock_lenght -- Длина кока сейчас
              #last_cock -- Дата последнего кручения
              #old_cock -- Крупнейший оторвавшийся кок
              #first_name -- Имя юзера
              #last_name -- Фамилия юзера
              #username -- Юзерка юзера
conn.close()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tg_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
async def top(stts):
    cockt_slov = {}
    conn = sq.connect('users.db')
    cur = conn.cursor()
    if stts == "top":
        cur.execute("SELECT * FROM tgusers ORDER BY cock_lenght DESC")
    elif stts == "atop":
        cur.execute("SELECT * FROM tgusers ORDER BY cock_lenght ASC")
    elif stts == "lngst":
        cur.execute("SELECT * FROM tgusers ORDER BY old_cock DESC")
    elif stts == "truet":
        cur.execute("SELECT * FROM tgusers WHERE last_cock >= ? ORDER BY cock_lenght DESC", (int(time()) - 604800,))
    result = cur.fetchmany(10)
    place = 1
    for x in result:
        user_num = str(x[2])
        if stts == "lngst":
            user_num = str(x[4])
        username = str(x[7])
        first_name = str(x[5])
        tgid = str(x[0])
        last_name = str(x[6])
        full_name = first_name
        if last_name != "None":
            full_name = full_name + " "+ last_name
        if username != "None" and first_name != "None":
            cockt_slov[str(place)] = [username, full_name, user_num, "FULLANDNAME"] # юзерка, фулл нейм, кок/отвал, тип
            place += 1
        elif username == "None" and first_name == "None":
            cockt_slov[str(place)] = [tgid,user_num,"ID"] # ид, кок/отвал, тип
            place += 1
        elif first_name == "None":
            cockt_slov[str(place)] = [username,user_num, "USERNAME"] # юзерка, кок/отвал, тип
            place += 1
        else:
            cockt_slov[str(place)] = [full_name,user_num, "FULLNAME"] # фулл нейм, кок/отвал, тип
            place += 1
    conn.close
    return cocktops(cockt_slov, stts)
    
async def chance(usercock: int):
    growth = randint(1, 20)
    chance = randint(0,100)
    if usercock >= 100 and randint(0,100) <= (usercock /100):
        return "otval"
    else:
        if chance >= 0 and chance <= 10 and usercock >= -1000:
            return growth * -1
        elif chance > 10 and chance <= 95:
            return growth
        elif chance > 95 and chance <= 100:
            return "x2"

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.from_user.id in blocked_ids:
        return
    await message.answer(startmsg)
    conn = sq.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
    userindb = cur.fetchall()
    if userindb == []:
        cur.execute('INSERT INTO tgusers (tgid, register_date, cock_lenght, last_cock, old_cock, first_name, last_name, username) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (message.from_user.id, int(time()), 0, 0, 0, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
        conn.commit()
    conn.close()
@dp.message_handler(commands=["profile","p","п","профиль"])
async def profiles(message: types.Message):
    
    conn = sq.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
    userindb = cur.fetchall()
    if userindb == []:
        cur.execute('INSERT INTO tgusers (tgid, register_date, cock_lenght, last_cock, old_cock, first_name, last_name, username) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (message.from_user.id, int(time()), 0, 0, 0, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
        conn.commit()
        userindb = cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
        userindb = cur.fetchall()

    
    db_tgid, db_reg_date, db_cock_lenght, db_last_cock, db_old_cock, db_first_name, db_last_name, db_username = userindb[0]
    if db_first_name == None:
        cur.execute('UPDATE tgusers SET first_name=?, last_name=?, username=? WHERE tgid=?', (message.from_user.first_name, message.from_user.last_name, message.from_user.username, db_tgid))
        conn.commit()
    conn.close()
    await message.reply(profile(db_reg_date, db_cock_lenght, db_last_cock, db_old_cock))
@dp.message_handler(commands=["кок", "cock"])
async def cock(message: types.Message):
    if message.from_user.id in blocked_ids:
        await message.reply(tb_access_denied)
        return
    msg = message.text.split(" ")
    if len(msg) == 2:
        if msg[1] in cock_top_aliases:
            await message.answer(await top("top"), disable_web_page_preview=True)
        elif msg[1] in cock_atop_aliases:
            await message.answer(await top("atop"), disable_web_page_preview=True)
        elif msg[1] in cock_lngst_aliases:
            await message.answer(await top("lngst"), disable_web_page_preview=True)
        elif msg[1] in cock_ttop_aliases:
            await message.answer(await top("truet"), disable_web_page_preview=True)
        else:
            await message.reply(tb_not_found)
    else:
        conn = sq.connect('users.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
        userindb = cur.fetchall()
        if userindb == []:
            cur.execute('INSERT INTO tgusers (tgid, register_date, cock_lenght, last_cock, old_cock, first_name, last_name, username) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (message.from_user.id, int(time()), 0, 0, 0, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
            conn.commit()
            cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
            userindb = cur.fetchall()
    
        userindb = userindb[0]
        db_tgid, db_reg_date, db_cock_lenght, db_last_cock, db_old_cock, db_first_name, db_last_name, db_username = userindb
        if db_last_cock+86340 <= int(time()):
            deystv = await chance(db_cock_lenght)
            if isinstance(deystv, int):
                db_cock_lenght += deystv
                if deystv > 0:
                    smbl = "+"
                else:
                    smbl = "-"
                msg = cockmsg(smbl, int(abs(deystv)), db_cock_lenght)
            else:
                if deystv == "x2":
                    db_cock_lenght = db_cock_lenght*2
                    msg = cockmsg("x2", db_cock_lenght)
                    
                else:
                    msg = cockmsg("otval", db_cock_lenght)
                    if db_old_cock < db_cock_lenght:
                        db_old_cock = db_cock_lenght
                    db_cock_lenght = 0
                    
            cur.execute('UPDATE tgusers SET cock_lenght=?, last_cock=?, old_cock=?, first_name=?, last_name=?, username=? WHERE tgid=?', (db_cock_lenght, int(time()), db_old_cock, message.from_user.first_name, message.from_user.last_name, message.from_user.username, db_tgid))
            conn.commit()
            conn.close()
            await message.reply(msg)
        else:
            msg_we = await message.reply(wait(db_last_cock + 86340 - int(time())))
            conn.close()
            await asyncio.sleep(10)
            try:
                await message.delete()
                await msg_we.delete()
            except:
                pass

@dp.message_handler(commands=["кокт", "top", "cockt", "топ"])
async def cocktop(message: types.Message):
    await message.answer(await top("top"), disable_web_page_preview=True)
        
@dp.message_handler(commands=["кокат", "atop", "cockat", "атоп"])
async def cockatop(message: types.Message):
    await message.answer(await top("atop"), disable_web_page_preview=True)
@dp.message_handler(commands=["коклт", "ltop", "cocklt", "лтоп"])
async def cockatop(message: types.Message):
    await message.answer(await top("lngst"), disable_web_page_preview=True)
@dp.message_handler(commands=["коктт", "ttop", "cocktt", "ттоп"])
async def cockatop(message: types.Message):
    await message.answer(await top("truet"), disable_web_page_preview=True)

@dp.message_handler(commands=["reset"])
async def cock(message: types.Message):
    msg = message.text.split()
    conn = sq.connect('users.db')
    cur = conn.cursor()
    if message.from_user.id in admin_ids:
        if len(msg) == 2:
            cur.execute('UPDATE tgusers SET cock_lenght=?, old_cock=? WHERE tgid=?', (0, 0, msg[1]))
            conn.commit()
            conn.close()
        if len(msg) == 3:
            if msg[2] == "full":
                cur.execute('UPDATE tgusers SET cock_lenght=?, last_cock=?, old_cock=? WHERE tgid=?', (0, 0, 0, msg[1]))
                conn.commit()
                conn.close()
    else:
        pass
@dp.message_handler(content_types=['new_chat_members'])
async def send_welcome(message: types.Message):
    bot_obj = await bot.get_me()
    bot_id = bot_obj.id
    for chat_member in message.new_chat_members:
        if chat_member.id == bot_id:
            await message.answer(tb_add_tochat)
#@dp.message_handler(commands=["update"]) ## ОБНОВИТЬ БД (юзернеймы) ИСПОЛЬЗОВАТЬ ОДИН РАЗ, так же можно использовать для дальнейших апдейтов, просто задокументировать
#async def top(message: types.Message):
#    conn = sq.connect('users.db')
#    cur = conn.cursor()
#    cur.execute("ALTER TABLE tgusers ADD COLUMN first_name 'TEXT'")
#    cur.execute("ALTER TABLE tgusers ADD COLUMN last_name 'TEXT'")
#    cur.execute("ALTER TABLE tgusers ADD COLUMN username 'TEXT'")
#    conn.commit()
#    conn.close()
#    await message.answer("done.")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
