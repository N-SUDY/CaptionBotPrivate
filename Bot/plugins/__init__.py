from pyrogram import Client, filters
from pyrogram.types import Message

x = []
PASS = ["cipherx"]

@app.on_message(filters.incoming & filters.private & ~filters.edited)
async def verifys(c: Client, m: Message):
    id = m.from_user.id
    if not id in x:
        verify = await c.ask(m.chat.id, "پسورد را وارد کنید")
        if verify.text in PASS:
            x.append(id) 
            await m.reply("شما به لیست ادمین ها افزوده شدید و هم اکنون میتوانید از بات استفاده نمایید", quote=True)
            return True 
        if not verify.text:
            await verify.reply("پسوردی یافت نشد", quote=True)
            return await verifys(c, m)
        if not verify.text in PASS:
            await verify.reply("پسورد اشتباه است و شما نمی‌توانید از بات استفاده نمایید", quote=True)
            return True
    else:
        pass
