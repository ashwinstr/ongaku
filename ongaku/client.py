from pyrogram import Client
from .config import Config

__all__=["Ongaku"]

class Ongaku(Client):
    def __init__(self, **kwargs):
        kwargs["api_id"]=Config.api_id
        kwargs["name"]="Ongaku-Bot"
        kwargs["session_string"]=Config.string_session
        kwargs["api_hash"]=Config.api_hash
        kwargs["device_model"]="Ongaku"
        kwargs["app_version"]=("git-" + Config.git_branch)
        kwargs["system_version"]=Config.operating_system
        kwargs["plugins"]=dict(root="ongaku.plugins")
        super().__init__(**kwargs)

    async def start(self):
        await super().start()