# All Credits Belong to @CipherXBot

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from Bot import app
from Bot.plugins import * 


@app.on_message(filters.command("start") & filters.incoming & filters.private & ~filters.edited)
async def start(c: Client , m: Message):
    firstname = m.from_user.first_name
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd.startswith("/start"):
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply(
                    text=f"""سلام {m.from_user.mention(style="md")} عزیز 🙋🏻‍♂️\nمن بات ادیت کپشن هستم\nفایل تلگرامی خود را ارسال کنید تا کپشن آن را ادیت کنم""",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton('✵ Developer ✵', url='https://t.me/CipherXBot')]
                        ]
                    ),
                    disable_web_page_preview=True
                ) 
        except Exception as e:
            return  


@app.on_message(filters.regex("راهنما") & filters.incoming & filters.private & ~filters.edited)
async def help(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "راهنما":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply("〄 راهنمای بات 〄\n✓ افزودن ادمین ✓ حذف ادمین ✓ لیست ادمین \n✓ افزودن پسورد ✓ حذف پسورد ✓ لیست پسورد\n✓ افزودن چنل ✓ حذف چنل ✓ لیست چنل \n✓ بفرس\n〄 همچنین با فرستادن هر فایل به بات می توانید کپشن آن را ادیت کنید.", quote=True) 
        except Exception as e:
            return


