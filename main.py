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
              (tgid TEXT, register_date INTEGER, cock_lenght INTEGER, last_cock INTEGER, old_cock)''')
cur.close()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tg_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

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
        else:
            return "x2"

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(startmsg)
    conn = sq.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
    userindb = cur.fetchall()
    if userindb == []:
        cur.execute('INSERT INTO tgusers (tgid, register_date, cock_lenght, last_cock, old_cock) VALUES (?, ?, ?, ?, ?)', (message.from_user.id, int(time()), 0, 0, 0))
        conn.commit()
    conn.close()

@dp.message_handler(commands=["кок", "cock"])
async def cock(message: types.Message):
    msg = message.text.split(" ")
    if len(msg) == 2:
        if msg[1] in cock_top_aliases:
            await message.answer(tb_indev(message.text))
        elif msg[1] in cock_atop_aliases:
            await message.answer(tb_indev(message.text))
        else:
            await message.answer(tb_not_found)
    else:
        conn = sq.connect('users.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
        userindb = cur.fetchall()
        if userindb == []:
            cur.execute('INSERT INTO tgusers (tgid, register_date, cock_lenght, last_cock, old_cock) VALUES (?, ?, ?, ?, ?)', (message.from_user.id, int(time()), 0, 0, 0))
            conn.commit()
            cur.execute('SELECT * FROM tgusers WHERE tgid = ?', (message.from_user.id,))
            userindb = cur.fetchall()
            conn.close()
    
        userindb = userindb[0]
        db_tgid, db_reg_date, db_cock_lenght, db_last_cock, db_old_cock = userindb
        deystv = await chance(db_cock_lenght)
        if isinstance(deystv, int):
            db_cock_lenght += deystv
            if deystv > 0:
                smbl = "+"
            else:
                smbl = "-"
            msg = cockmsg(smbl, int(abs(deystv)))
        else:
            if deystv == "x2":
                db_cock_lenght = db_cock_lenght*2
                msg = cockmsg("x2", db_cock_lenght)
                
            else:
                msg = cockmsg("otval", db_cock_lenght)
                if db_old_cock < db_cock_lenght:
                    db_old_cock = db_cock_lenght
                db_cock_lenght = 0
                
        cur.execute('UPDATE tgusers SET cock_lenght=?, last_cock=?, old_cock=? WHERE tgid=?', (db_cock_lenght, int(time()), db_old_cock, db_tgid))
        conn.commit()
        conn.close()
        await message.answer(msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
