from pyrogram import Client, filters
from pyrogram.types import Message

ADMINS = []
PASS = ["cipherx"]


async def verifys(c: Client, m: Message):
    id = m.from_user.id
    if id not in ADMINS:
        verify = await c.ask(m.chat.id, "پسورد را وارد کنید")
        if verify in PASS:
            ADMINS.append(id) 
            await m.reply("شما به لیست ادمین ها افزوده شدید و هم اکنون میتوانید از بات استفاده نمایید", quote=True) 
        if not verify.text:
            await verify.reply("پسوردی یافت نشد", quote=True)
            return await verifys(c, m)
    if not verify in PASS:
        await caption.reply("پسورد اشتباه است و شما نمی‌توانید از بات استفاده نمایید", quote=True)
        return True
