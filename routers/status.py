from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from database.auth import get_key
from filters import AuthFilter
from server import get_readings
from templates import *

router = Router()


@router.message(Command("status"), AuthFilter())
@router.message(F.text == BUTTON_STATUS, AuthFilter())
async def cmd_status(message: Message):
    values = get_readings(get_key(message.from_user.id))
    await message.answer(
        MESSAGE_STATUS.format(values[0] or MISSING_VALUE, values[1] or MISSING_VALUE, values[2] or MISSING_VALUE)
    )
