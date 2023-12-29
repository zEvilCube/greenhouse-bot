from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.auth import register_key
from routers.menu import command_menu
from server import verify_auth
from states import AuthStates
from templates import *

router = Router()


@router.message(Command("auth"))
@router.message(F.text == BUTTON_AUTH)
async def command_auth(message: Message, state: FSMContext):
    await state.set_state(AuthStates.PENDING_AUTH)
    await message.answer(MESSAGE_PENDING_AUTH)


@router.message(AuthStates.PENDING_AUTH)
async def pending_auth(message: Message, state: FSMContext):
    if verify_auth(message.text):
        register_key(message.from_user.id, message.text)
        return await command_menu(message, state)
    await message.answer("Неверный ключ. Попробуйте ещё раз:")
