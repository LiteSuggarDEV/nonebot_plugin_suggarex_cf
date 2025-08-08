from collections.abc import Iterable
from typing import Any

import aiohttp
from aiohttp import ClientSession
from nonebot import get_driver, logger
from nonebot_plugin_suggarchat.API import ModelAdapter, config_manager
from pydantic import BaseModel


class ResponseData(BaseModel):
    """
    Cloudflare API 响应数据模型
    """

    response: str


class Response(BaseModel):
    """
    Cloudflare API 响应模型
    """

    result: ResponseData
    success: bool
    messages: list[str]
    errors: list[str]


class CloudflareAdapter(ModelAdapter):
    """
    Cloudflare AI 适配器
    """

    async def call_api(self, messages: Iterable[Any]) -> str:
        config = self.config
        preset = self.preset
        key = preset.api_key
        model = preset.model
        user_id = getattr(preset.extra, "cf_user_id") or getattr(
            config.default_preset.extra, "cf_user_id"
        )
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
                    response.raise_for_status()

                data = Response.model_validate(await response.json())
                if not data.success:
                    raise Exception((data.errors, data.messages))
                return data.result.response
            except Exception as e:
                logger.error(f"{e}")
                logger.error("请求失败！")
                raise e

    @staticmethod
    def get_adapter_protocol() -> str | tuple[str, ...]:
        return "cloudflare", "cf"


driver = get_driver()


@driver.on_startup
async def hook():
    """
    启动时注册
    """

async def init_config():
    """
    注册配置项
    """
    config_manager.reg_model_config("cf_user_id", "")
