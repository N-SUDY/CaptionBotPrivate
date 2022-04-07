from pyrogram import Client, filters
from pyrogram.types import Message

from Bot import app
from Bot.plugins import x, PASS, verifys 


@app.on_message(filters.incoming & filters.private & ~filters.edited)
async def passphrase(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd.startswith("پسورد"):
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                PASS.append(p)
                if not p.text:
                    await p.reply("پسوردی یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                     return True 
        except Exception as e:
            return 

@app.on_message(filters.incoming & filters.private & ~filters.edited)
async def show_list(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd.startswith("نمایش لیست"):
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                for i in x:
                    await m.reply(f"{i}", quote=True) 
        except Exception as e:
            return 
