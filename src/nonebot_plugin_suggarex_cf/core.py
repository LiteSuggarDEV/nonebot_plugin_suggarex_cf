import aiohttp
from aiohttp import ClientSession
from nonebot import get_driver, logger
from nonebot.adapters import Bot

from nonebot_plugin_suggarchat.API import Adapter, config_manager
from nonebot_plugin_suggarchat.config import Config
from nonebot_plugin_suggarchat.hook_manager import register_hook


async def adapter(
    base_url: str,
    model: str,
    key: str,
    messages: list,
    max_tokens: int,
    config: Config,
    bot: Bot,
) -> str:
    if config.preset == "__main__":
        user_id = config.cf_user_id
    else:
        models = config_manager.get_models()
        for m in models:
            if m.name == config.preset:
                user_id = m.cf_user_id
                break
        else:
            user_id = config.cf_user_id
            logger.warning(f"模型 {config.preset} 未找到，使用默认配置 {user_id}")
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {key}",
    }
    if model.startswith("@"):
        model = model.replace("@", "")
    if not key:
        raise ValueError("请配置Cloudflare API Key")

    async with ClientSession(
        headers=headers,
        timeout=aiohttp.ClientTimeout(total=25),
    ) as session:
        try:
            response = await session.post(
                url=f"https://api.cloudflare.com/client/v4/accounts/{user_id}/ai/run/@{model}",
                json={"messages": messages},
            )
            if response.status != 200:
                logger.error(f"请求失败！user{user_id}/模型 {model}")
                raise Exception(f"{response.status}\n{response.text}")

            data = await response.json()
            return data["result"]["response"]
        except Exception as e:
            logger.error(f"{e}")
            logger.error("请求失败！")
            raise e


driver = get_driver()


@driver.on_startup
async def hook():
    """
    启动时注册
    """
    register_hook(init_config)


async def init_config():
    """
    注册配置项
    """
    ada = Adapter()

    config_manager.register_config("cf_user_id")
    config_manager.reg_model_config("cf_user_id")
    ada.register_adapter(adapter, "cf")
