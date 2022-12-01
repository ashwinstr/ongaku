"""

 * file_extensions.py: File to provide known name extensions to Ongaku

  Copyright (C) 2022 Shouko

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
import os
from subprocess import run


class Config:
    api_hash=os.environ.get("API_HASH")
    api_id =os.environ.get("API_ID")
    string_session=os.environ.get("STRING_SESSION")
    log_channel = os.environ.get("LOG_CHANNEL")
    bio_ = ""
    music_player = [os.environ.get("MUSIC_PLAYER")]
    looper = os.environ.get("LOOP")
    current_ = ["dummy"]
    users = [int(i) for i in os.environ.get("USERS").split(",")]
    trigger = os.environ.get("CMD_TRIGGER") or "."
    git_branch = run("git branch --show-current", shell=True, capture_output=True).stdout.decode("utf-8")
    operating_system = run("uname -srmo", shell=True, capture_output=True).stdout.decode("utf-8")
    EXTENTIONS = ".aac" ".amr" ".mp3" ".m4a" ".ogg" ".opus" ".wav" ".wma"
    BLOAT = [
        "hq",
        "hd",
        "high quality",
        "audio",
        "(audio)",
        "audio only",
        "(audio only)",
        "explicit",
        "clean",
        "short version",
        "long version",
        "(lyrics)",
        "official audio",
        "[official audio]",
        "(official audio)",
        "(official)",
        "(official music video)",
        "(Official Video - Clean Version)",
        "explicit",
        "(explicit)",
        "(explicit music video)",
        "album",
        "full version",
        "(dirty)",
        "(dirty version)",
        "(uncensored lyrics)",
        "(uncensored)",
        "uncensored version",
        "(uncensored version)",
        "playlist",
        "(playlist)",
        "live",
        "(live)",
        "(Lofi)",
        "(lo-fi)",
        "(slowed)",
        "(reverbed)",
        "(slow)",
        "(reverb)",
        "(slowed & reverb)",
        "(remix)",
        "(mashup)",
    ]
