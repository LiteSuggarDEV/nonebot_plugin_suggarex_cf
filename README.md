# nonebot_plugin_suggarex_cf
CloudFlare Workers AI Proctol Adapter for SuggarChat

## 适用于SuggarChat插件的CloudFlare协议适配器实现

[SuggarChat](https://github.com/JohnRichard4096/nonebot_plugin_suggarchat)

## 安装

```bash
pip install nonebot-plugin-suggarex-cf
```

## 配置文件
额外添加了 `cf_user_id` 配置项，，用于标识 CloudFlare Worker 的用户，默认为 null

## 使用
将协议更改为 `cf` 将可以通过提供的token 访问 CloudFlare Workers AI 接口,具体配置请参考Suggar的配置文件说明。