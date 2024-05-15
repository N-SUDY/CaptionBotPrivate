# All Credits Belong to @CipherXBot

from pyrogram import Client, filters
from pyrogram.types import Message

from Bot import app
from Bot.plugins import *


@app.on_message(filters.private & filters.media, group=4)
async def incoming(c: Client, m: Message):
    id = m.from_user.id
    try:
        if not id in x:
            vf = await verifys(c, m) 
        else:
            caption = await get_caption(c, m)
            if caption is True:
                return
            await m.copy(chat_id=m.chat.id, caption=caption, reply_to_message_id=m.id)
    except Exception as e:
        return


async def get_caption(c: Client, m: Message):
    caption = await c.ask(m.chat.id, "Send your caption. Write `cancel` to cancel this process")
    if not caption.text:
        await caption.reply("No caption found", quote=True)
        return await get_caption(c, m)
    if caption.text.startswith("cancel"):
        await caption.reply("Process canceled", quote=True)
        return True
    else:
        return caption.text
