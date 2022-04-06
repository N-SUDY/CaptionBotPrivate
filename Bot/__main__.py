import glob
import asyncio
import logging
import time
import os
import sys
import importlib
import re
from pathlib import Path

from pyrogram import Client, errors, idle

from Bot import app
from Bot.config import Var

DOWNLOAD_LOCATION = "./Downloads"

StartTime = time.time()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

ppath = "Bot/plugins/*.py"
files = glob.glob(ppath)

loop = asyncio.get_event_loop()

async def start_services():
    print('\n')
    print('------------------- Initalizing Caption Bot -------------------')
    await app.start()
    print('----------------------------- DONE -----------------------------')
    print('\n')
    print('--------------------------- Importing ---------------------------')
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
            print("Imported => " + plugin_name)
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
