from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.auth import get_key
from routers.auth import command_auth


class AuthFilter(BaseFilter):
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        user_id = message.from_user.id
        if get_key(user_id) is not None:
            return True
        await command_auth(message, state)
        return False


class LightFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not message.text.isdigit() or not (0 <= int(message.text) <= 1000):
            await message.reply("Неверное значение (0-1000)")
            return False
        return True


class TempFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not message.text.isdigit() or not (20 <= int(message.text) <= 40):
            await message.reply("Неверное значение (20-40)")
            return False
        return True


class HumidityFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not message.text.isdigit() or not (0 <= int(message.text) <= 100):
            await message.reply("Неверное значение (0-100)")
            return False
        return True


