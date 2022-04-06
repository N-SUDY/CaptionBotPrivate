from pyrogram import Client
from pyromod import listen

from Bot.config import Var

app = Client(
    session_name='Caption',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=60,
    workers=4
)
