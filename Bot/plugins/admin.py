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

@app.on_message(filters.user(ADMINS) & filters.regex("پسورد") & filters.incoming & filters.private & ~filters.edited) 
async def passphrase(c: Client, m: Message):
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd.startswith("پسورد"):
        pass = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
        PASS.append(pass)
        if not pass.text:
            await pass.reply("پسوردی یافت نشد", quote=True) 
        if pass.text.startswith("کنسل"):
            return True 
        else:
            return pass.text
