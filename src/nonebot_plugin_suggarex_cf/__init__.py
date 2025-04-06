from nonebot.plugin import PluginMetadata, require

from . import core


require("nonebot_plugin_suggarchat")


__all__ = ["core"]

__plugin_meta__ = PluginMetadata(
    name="SuggarChat CloudFlare协议扩展附属插件",
    description="适用于SuggarChat插件的CloudFlare协议适配器实现，SuggarChat附属插件",
    usage="",
    type="library",
    homepage="https://github.com/LiteSuggarDEV/nonebot_plugin_suggarex_cf",
    supported_adapters={"~onebot.v11"},
)
