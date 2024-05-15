# All Credits Belong to @CipherXBot

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from Bot import app
from Bot.plugins import *


@app.on_message(filters.command("start") & filters.incoming & filters.private)
async def start(c: Client , m: Message):
    firstname = m.from_user.first_name
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd.startswith("/start"):
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply(
                    text=f"Hello {m.from_user.mention(style='md')} 🙋🏻‍♂️\nI'm a Caption Editor Bot\nSend your Telegram file so I can edit its caption.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton('✵ Developer ✵', url='https://t.me/CipherXBot')]
                        ]
                    ),
                    disable_web_page_preview=True
                ) 
        except Exception as e:
            return  


@app.on_message(filters.regex("help") & filters.incoming & filters.private)
async def help(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "help":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply("〄 Bot Help 〄\n✓ Add Channel\n✓ Send\n✓ ID\n〄 Also, you can edit the caption of any file by sending it to the bot.", quote=True) 
        except Exception as e:
            return
