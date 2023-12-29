from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters import AuthFilter
from routers.menu import command_menu
from templates import *

router = Router()


@router.message(Command("start"))
async def command_start(message: Message, state: FSMContext):
    await message.answer(MESSAGE_GREETING.format(message.from_user.full_name))
    await command_menu(message, state)


@router.message(Command("help"))
async def command_help(message: Message):
    await message.answer(MESSAGE_HELP)
