# client.py

import asyncio
import os
import sys
from subprocess import run

from pyrogram import Client
from ..config import Config
from ..song import get_song

looper = os.environ.get("LOOP")
users = [int(i) for i in os.environ.get("USERS").split(",")]
trigger = os.environ.get("CMD_TRIGGER")

git_branch = run(
    "git branch --show-current", shell=True, capture_output=True
).stdout.decode("utf-8")

operating_system = run("uname -srmo", shell=True, capture_output=True).stdout.decode("utf-8")


class Ongaku(Client):

    def __init__(self, **kwargs):
        kwargs['name'] = "kakashi's test"
        kwargs['api_id'] = Config.API_ID
        kwargs['api_hash'] = Config.API_HASH
        kwargs['bot_token'] = Config.BOT_TOKEN
        super().__init__(**kwargs)

    async def start(self):
        await super().start()
        await self.loop_()

    async def stop(self):
        await super().stop()

    async def loop_(self):
        if Config.LOG_CHANNEL:
            await self.send_message(Config.LOG_CHANNEL, "`Kakashi's ongaku started...`")
        print("Ongaku started...\nNotifications are checked every 30 seconds.")
        me = await self.get_chat("me")
        global bio
        bio = me.bio if me.bio else ""
        while True:
            song = await get_song()
            if (
                song not in ["Ongaku: No notification detected",
                             "Ongaku: Bio update skipped: Notification is stale"]
                and Config.LOG_CHANNEL
            ):
                await self.send_message(Config.LOG_CHANNEL, song)
            if song == "Ongaku: No notification detected" and looper.lower() != "yes":
                await self.update_profile(bio)
                print("Notification not detected.")
                sys.exit()
            await asyncio.sleep(30)