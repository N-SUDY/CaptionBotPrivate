# All Credits Belong to @CipherXBot

from pyrogram import Client, filters
from pyrogram.types import Message 

x = []
list1 = [] 
list2 = [] 
PASS = ["ok"]


async def verifys(c: Client, m: Message):
    id = m.from_user.id
    if not id in x:
        verify = await c.ask(m.chat.id, "پسورد را وارد کنید")
        if verify.text in PASS:
            x.append(id) 
            await m.reply("شما به لیست ادمین ها افزوده شدید و هم اکنون میتوانید از بات استفاده نمایید", quote=True)
            return id
        if not verify.text:
            await verify.reply("پسوردی یافت نشد", quote=True)
            return await verifys(c, m)
        if not verify.text in PASS:
            await verify.reply("پسورد اشتباه است و شما نمی‌توانید از بات استفاده نمایید", quote=True)
            return True
    else:
        pass


async def chad(c: Client, m: Message):
    if list1 and list2: 
        dic = dict(zip(list1, list2))
        return dic
