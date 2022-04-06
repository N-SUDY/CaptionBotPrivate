import asyncio,os

from pyrogram.types.messages_and_media import message
from pyromod import listen 
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from Bot import app

@app.on_message(filters.private & filters.media & ~filters.edited, group=4)
async def incoming(c: Client, m: Message):
    name=None
    if m.photo:
      file=m.photo.file_id
      type_="pic"
    elif m.video:
      file=m.video.file_id
      type_="video"
    elif m.document:
      file=m.document.file_id
      type_="document"
    elif m.audio:
      file=m.audio.file_id
      type_="audio"
    else:
      return await m.reply("UnSupported File")
    await c.edit_message_caption(chat_id=m.chat.id, message_id=m.message_id, caption=caption)
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
