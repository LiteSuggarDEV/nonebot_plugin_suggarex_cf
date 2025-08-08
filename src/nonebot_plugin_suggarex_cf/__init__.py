from nonebot.plugin import PluginMetadata, require

require("nonebot_plugin_suggarchat")

from . import core

__all__ = ["core"]

__plugin_meta__ = PluginMetadata(
    name="SuggarChat CloudFlare扩展",
    description="SuggarChat的CloudFlare WorkersAI API接口扩展",
    usage="",
    type="library",
    homepage="https://github.com/LiteSuggarDEV/nonebot_plugin_suggarex_cf",
    supported_adapters={"~onebot.v11"},
)
