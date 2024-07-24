import httpx
import json
from controller.message_dto import MessageDTO
from controller.bot.controll import bot_topic
from const import CLIENT_PORTS, POST_ERROR_LOG


class ForeignApi:

    # отправка сообщения на сторонний сервис, учитывая социальную сеть
    async def send_message_out(self, message: MessageDTO):
        port = CLIENT_PORTS[message.social]
        try:
            await self._send_post_request(
                f'http://127.0.0.1:{port}/', 
                message.model_dump_json()
            )
        except Exception as e:
            await bot_topic.log(
                POST_ERROR_LOG.format(
                    social=message.social,
                    error=e,
                )
            )

    # отправляет post-запросс по url с указаными данными 
    @staticmethod
    async def _send_post_request(url: str, data: json):
        async with httpx.AsyncClient() as client:
            return await client.post(url, data=data)


foreign_api = ForeignApi()
