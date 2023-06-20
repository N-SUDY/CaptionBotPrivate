# All Credits Belong to @CipherXBot

import glob
import asyncio
import logging
import time
import os
import signal
import sys
import importlib
import re
from pathlib import Path

from pyrogram import Client, errors, idle

from Bot import app
from Bot.config import Var


logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(name)s][%(levelname)s] ==> %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout),
              logging.FileHandler("captionbot.log", mode="a", encoding="utf-8")],)

logging.getLogger("pyrogram").setLevel(logging.INFO)


ppath = "Bot/plugins/*.py"
files = glob.glob(ppath)


loop = asyncio.get_event_loop()


async def start_services():
    logging.info('-------- Initalizing Caption Bot --------')
    await app.start()
    bot_info = await app.get_me()
    logging.debug(bot_info)
    app.username = bot_info.username
    logging.info("bot =>> {}".format(bot_info.first_name))
    if bot_info.dc_id:
        logging.info("DC ID =>> {}".format(str(bot_info.dc_id)))
    logging.info('------------------- DONE --------------------')
    logging.info('\n')
    logging.info('------------- Importing Plugins ------------')
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"Bot/plugins/{plugin_name}.py")
            import_path = ".plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["Bot.plugins." + plugin_name] = load
            logging.info("Imported => " + plugin_name)
    logging.info('----------- Caption Bot is Ready to Use ------------')
    await idle()
    
    
async def cleanup():
    await server.cleanup()
    if app.is_connected:
        await app.stop()
        
async def handle_termination(signum, frame):
    print("Received termination signal")
    await cleanup()
    sys.exit(0)
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda s,f: asyncio.ensure_future(handle_termination(s,f)))
    signal.signal(signal.SIGTERM, lambda s,f: asyncio.ensure_future(handle_termination(s,f)))
    try:
        loop.run_until_complete(start_services())
        loop.run_forever()
    except KeyboardInterrupt:
        print("------------------------ Stopped Services ------------------------")
