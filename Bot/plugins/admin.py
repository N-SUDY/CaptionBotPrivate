from pyrogram import Client, filters
from pyrogram.types import Message

from Bot import app
from Bot.plugins import x, PASS, verifys

@app.on_message(filters.incoming & filters.private & ~filters.edited)
async def add_admin(c: Client, m: Message):
    await verifys(c, m) 

@app.on_message(filters.user(*x) & filters.regex("پسورد") & filters.incoming & filters.private & ~filters.edited)
async def passphrase(c: Client, m: Message):
    cmd = m.text.split("_")[-1]
    if cmd.startswith("پسورد"):
        p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
        PASS.append(p)
        if not p.text:
            await p.reply("پسوردی یافت نشد", quote=True) 
        if p.text.startswith("کنسل"):
            return True 

@app.on_message(filters.command("show") & filters.incoming & filters.private & ~filters.edited)
async def show_list(c: Client, m: Message):
    cmd = m.text.split("_")[-1]
    if cmd.startswith("/show"):
        await m.reply(f"{x}", quote=True) 
