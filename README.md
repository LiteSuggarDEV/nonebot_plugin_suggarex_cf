# nonebot_plugin_suggarex_cf
CloudFlare Workers AI Proctol Adapter for SuggarChat

## 适用于SuggarChat插件的CloudFlare协议适配器实现

[SuggarChat](https://github.com/LiteSuggarDEV/nonebot_plugin_suggarchat)

## 安装

-   方法1
    ```bash
    nb plugin install nonebot_plugin_suggarex_cf
    ```
-   方法2
    ```bash
    pip install nonebot-plugin-suggarex-cf
    ```
    如果使用**方法2**,就需要在pyproject.toml中的plugins列表中作如下处理：
    ```toml
    plugins=["nonebot_plugin_suggarex_cf"]
    # 添加"nonebot_plugin_suggarex_cf"
    ```

## 配置文件
额外添加了 `cf_user_id` 配置项，用于标识 CloudFlare Worker 的用户，默认为 null，请在WorkersAI主页找到你的用户ID并填写！

## 使用
将协议(`protocol`字段的值)更改为 `cf` 将可以通过提供的token 访问 CloudFlare Workers AI 接口,模型请填写CloudFlare Workers AI的**文本生成模型**,并不*需要使用* **@** *拼接*,例如`"model":"llama-3.2-xxxx"`.具体配置请参考Suggar的配置文件说明。