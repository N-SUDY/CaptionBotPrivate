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
        verify = await m.chat.ask("Enter the password:")
        if verify.text in PASS:
            x.append(id) 
            await m.reply("You have been added to the admin list and can now use the bot.", quote=True)
            return id
        if not verify.text:
            await verify.reply("Password not found.", quote=True)
            return await verifys(c, m)
        if not verify.text in PASS:
            await verify.reply("Incorrect password, you cannot use the bot.", quote=True)
            return True
    else:
        pass


async def chad(c: Client, m: Message):
    if list1 and list2: 
        dic = dict(zip(list1, list2))
        return dic
