from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from routers.menu import command_menu
from routers.model import command_model
from states import MenuStates, ModelStates
from templates import BUTTON_BACK

router = Router()


@router.message(F.text == BUTTON_BACK, ModelStates.PENDING_LIGHTING)
@router.message(F.text == BUTTON_BACK, ModelStates.PENDING_TEMPERATURE)
@router.message(F.text == BUTTON_BACK, ModelStates.PENDING_HUMIDITY)
async def back_model(message: Message, state: FSMContext):
    await command_model(message, state)


@router.message(F.text == BUTTON_BACK)
async def back_menu(message: Message, state: FSMContext):
    await command_menu(message, state)
