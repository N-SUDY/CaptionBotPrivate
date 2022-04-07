from pyrogram import Client, filters
from pyrogram.types import Message

from Bot import app
from Bot.plugins import * 

@app.on_message(filters.user(ADMINS) & filters.private & filters.media & ~filters.edited, group=4)
async def incoming(c: Client, m: Message):
    caption = await get_caption(c, m)
    if caption is True:
        return
    await m.copy(chat_id=m.chat.id, caption=caption, reply_to_message_id=m.message_id)

async def get_caption(c: Client, m: Message):
    caption = await c.ask(m.chat.id, "کپشن خود را ارسال نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
    if not caption.text:
        await caption.reply("کپشنی یافت نشد", quote=True)
        return await get_caption(c, m)
    if caption.text.startswith("کنسل"):
        await caption.reply("فرایند کنسل شد", quote=True)
        return True
    else:
        return caption.text 
