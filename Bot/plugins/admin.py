from pyrogram import filters

from Bot import app
from Bot.plugins import * 

@app.on_message(filters.incoming & filters.private & ~filters.edited)
async def add_admin(c: Client, m : Message):
    id = m.from_user.id
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == PASS:
        ADMINS.append(id)
        await m.reply("شما به لیست ادمین ها افزوده شدید و هم اکنون می توانید از بات استفاده نمایید") 
    else:
        return 


@app.on_message(filters.user(ADMINS) & filters.command('پسورد') & filters.incoming & filters.private & ~filters.edited)
async def pass(c: Client, m : Message):
    pass = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
    if not pass.text:
        await pass.reply("پسوردی یافت نشد", quote=True)
        await PASS.append(pass)
    if pass.text.startswith("کنسل"):
        await pass.reply("فرایند کنسل شد", quote=True)
        return True
