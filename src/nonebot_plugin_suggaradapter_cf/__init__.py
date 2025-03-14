from nonebot.plugin import PluginMetadata
from nonebot.plugin import require, PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="适用于SuggarChat的CloudFlare Workers AI 协议适配器",
    description="CloudFlare Adapter for suggarchat",
    usage="",
    type="library",
    homepage="https://github.com/JohnRichard4096/nonebot_plugin_suggaradapter_cf",
    supported_adapters={"~onebot.v11"},
)

require("nonebot_plugin_suggarchat")

from .core import *
