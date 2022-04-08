# All Credits Belong to @CipherXBot 

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid

from Bot import app
from Bot.plugins import *


@app.on_message(filters.regex("بفرس") & filters.incoming & filters.private & ~filters.edited)
async def send(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "بفرس":
        msg = await c.ask(m.chat.id, "بر روی فایل مورد نظر خود ریپلای کنید تا آن را برایتان به چنل داخواهتان در لیست چنل های اضافه شده بفرستم") 
        msg = msg.reply_to_message
        if msg:
            chat = await c.ask(m.chat.id, "اکنون چت آیدی چنل مورد نظر خود را بفرستید. شما میتوانید چت آیذی چنل مورد نظر خود را از لیست چنل دریافت نمایید") 
            if chat.text.startswith("-100"):
                await msg.copy(chat_id=m.chat.id)
            else:
                await chat.reply("لطفا چت آیدی صحیح را وارد نمایید", quote=True) 
        else:
            await msg.reply("شما بر روی فایل مورد نظر خود ریپلای نکردید", quote=True) 


@app.on_message(filters.regex("لیست چنل") & filters.incoming & filters.private & ~filters.edited)
async def show_channels(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست چنل":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                mad = await chad(c, m) 
                await m.reply(f"{mad}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن چنل") & filters.incoming & filters.private & ~filters.edited)
async def add_channel(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن چنل":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی چنل مورد نظر خود را وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل") and p.text.startswith("-100"):
                    try:
                        list1.append((await app.get_chat(int(p.text))).title)
                        list2.append(int(p.text))
                        await chad(c, m) 
                        await p.reply("چنل جدید با موفقیت افزوده شد", quote=True) 
                    except ChannelInvalid:
                        await p.reply("ابتدا بات را در چنل ادمین کرده و سپس چت آیدی آن را بفرستید", quote=True)
                if not p.text.startswith("-100") and p.text != "کنسل":
                    await p.reply("لطفا فقط چت عددی چنل وارد نمایید", quote=True)  
                if not p.text and not p.text.startswith("کنسل"):
                    await p.reply("چت آیدی یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 

@app.on_message(filters.regex("حذف چنل") & filters.incoming & filters.private & ~filters.edited)
async def rem_channel(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف چنل":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "چت آیدی مورد نظر خود را برای حذف چنل وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    if p.text.startswith("-100"):
                        if not int(p.text) in list2:
                            await p.reply("چت آیدی در لیست چنل ها یافت نشد", quote=True)  
                        else:
                            await chad(c, m) 
                            list1.remove((await app.get_chat(int(p.text))).title)
                            list2.remove(int(p.text))
                            dict.pop((await app.get_chat(int(p.text))).title)
                            await m.reply("چنل با موفقیت حذف شد", quote=True) 
                    if not p.text.startswith("-100"): 
                        await p.reply("لطفا فقط چت آیدی وارد نمایید", quote=True) 
                else:  
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("لیست ادمین") & filters.incoming & filters.private & ~filters.edited)
async def show_admins(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply(f"{x}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن ادمین") & filters.incoming & filters.private & ~filters.edited)
async def add_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل") and p.text.isnumeric() is True:
                    x.append(int(p.text))
                    await p.reply("ادمین جدید با موفقیت افزوده شد", quote=True) 
                if p.text.isnumeric() is False and p.text != "کنسل":
                    await p.reply("لطفا فقط آیدی عددی وارد نمایید", quote=True) 
                if not p.text and not p.text.startswith("کنسل"):
                    await p.reply("آیدی یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("حذف ادمین") & filters.incoming & filters.private & ~filters.edited)
async def rem_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی مورد نظر خود را برای حذف ادمین و عدم دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    if p.text.isnumeric() is True:
                        if not int(p.text) in x:
                            await p.reply("آیدی در لیست ادمین ها یافت نشد", quote=True)  
                        else:
                            x.remove(int(p.text))
                            await p.reply("ادمین با موفقیت حذف شد", quote=True) 
                    if p.text.isnumeric() is False: 
                        await p.reply("لطفا فقط آیدی عددی وارد نمایید", quote=True) 
                else:  
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("لیست پسورد") & filters.incoming & filters.private & ~filters.edited)
async def show_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply(f"{PASS}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن پسورد") & filters.incoming & filters.private & ~filters.edited)
async def add_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    PASS.append(p.text)
                    await p.reply("پسورد جدید با موفقیت افزوده شد", quote=True) 
                if not p.text:
                    await p.reply("پسوردی یافت نشد", quote=True) 
                else:
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("حذف پسورد") & filters.incoming & filters.private & ~filters.edited)
async def rem_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای حذف و عدم دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    if not p.text in PASS:
                        await p.reply("پسورد در لیست پسورد ها یافت نشد", quote=True)  
                    else:
                        PASS.remove(p.text)
                        await p.reply("پسورد با موفقیت حذف شد", quote=True) 
                if not p.text and not p.text.startswith("کنسل"):
                    await p.reply("پسورد یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 
