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
