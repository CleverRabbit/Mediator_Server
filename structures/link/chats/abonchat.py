from controller import MessageDTO
from controller import foreign_api


class AbonChat:
    
    def __init__(self, social: str, chat_id: int):
        self.social: str = social
        self.id: int = chat_id

    # фабричный метод создания объекта
    @classmethod
    def restore(cls, **kwargs):
        return cls(
            social=kwargs.get('social'),
            chat_id=kwargs.get('abon_id'),
        )

    # отправка сообщения в чат абонента
    async def send(self, message_dto: MessageDTO):
        message_dto.social = self.social
        message_dto.chat_id = self.id
        await foreign_api.send_message_out(message_dto)
