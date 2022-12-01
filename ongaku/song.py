# song.py

import re
import json
import os
from subprocess import run

from ongaku import venom, Config
from .file_extensions import Xtra

music_player = os.environ.get("MUSIC_PLAYER")
current_ = ['dummy']
bio = ""


async def get_song():
    title, content, val = "", "", "Ongaku: No notification detected"
    rw_data = run(
        "termux-notification-list", shell=True, capture_output=True
    ).stdout.decode("utf-8")
    for data in json.loads(rw_data):
        if data["packageName"] in music_player:
            # title, content = data["title"].strip(Xtra.EXTENTIONS), data[
            # "content"
            # ].strip(Xtra.EXTENTIONS)
            title, content = data["title"], data["content"]
            raw_title = f"{content} - {title}".replace("_", " ").strip("- ")
            for i in Xtra.BLOAT:
                remove_bloat = re.compile(re.escape(i), re.IGNORECASE)
                raw_title = remove_bloat.sub("", raw_title)
            remove_space = re.compile(re.escape("  "), re.IGNORECASE)
            raw_title = remove_space.sub("", raw_title)
            full = f"▷Now listening: {raw_title}"
            val = full
            if raw_title != current_[-1]:
                if len(val) > 70:
                    val = f"▷Now listening: {title}"
                    if len(val) > 70:
                        val = f"▷{title}"
                        if len(val) > 70:
                            val = val[0:70:]
                await venom.update_profile(bio=val)
                current_.append(raw_title)
                print(f" ▷ {raw_title}")
            else:
                val = "Ongaku: Bio update skipped: Notification is stale"
                # print (val)
    return val


async def reset_bio():
    print("\n\nOngaku: Resetting bio")
    await venom.update_profile(bio=bio)
    if Config.LOG_CHANNEL:
        return await venom.send_message(
            chat_id=int(Config.LOG_CHANNEL), text="Ongaku: Stopped"
        )