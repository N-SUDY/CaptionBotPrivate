# All Credits Belong to @CipherXBot

import asyncio

from pyrogram import Client
from pyrogram.types import Message 

from pyromod import listen

from Bot.config import Var

app = Client(
    "Caption",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=60,
    workers=4
)

async def pyromod_is_shit(c: Client, m: Message):
    if m.from_user is None:
        _id = m.sender_chat.id
        return _id
    else:
        _id = m.from_user.id
        return _id
