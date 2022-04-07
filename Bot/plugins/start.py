from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from Bot import app
from Bot.plugins import * 

@app.on_message(filters.incoming & filters.private & ~filters.edited)
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



