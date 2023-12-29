from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.auth import get_key
from filters import AuthFilter, LightFilter, TempFilter, HumidityFilter
from keyboards import get_back_keyboard, get_model_keyboard
from server import get_references, change_references
from states import MenuStates, ModelStates
from templates import *

router = Router()


@router.message(Command("model"), AuthFilter())
@router.message(F.text == BUTTON_MODEL, AuthFilter())
async def command_model(message: Message, state: FSMContext):
    values = get_references(get_key(message.from_user.id))
    await state.set_state(MenuStates.IN_MODEL_MENU)
    await message.answer(
        MESSAGE_MODEL.format(values[0] or UNSET_VALUE, values[1] or UNSET_VALUE, values[2] or UNSET_VALUE),
        reply_markup=get_model_keyboard()
    )


@router.message(F.text == BUTTON_LIGHTING, AuthFilter())
async def button_change_lighting(message: Message, state: FSMContext):
    await state.set_state(ModelStates.PENDING_LIGHTING)
    await message.answer(MESSAGE_PENDING_MODEL, reply_markup=get_back_keyboard())


@router.message(F.text == BUTTON_TEMPERATURE, AuthFilter())
async def button_change_temperature(message: Message, state: FSMContext):
    await state.set_state(ModelStates.PENDING_TEMPERATURE)
    await message.answer(MESSAGE_PENDING_MODEL, reply_markup=get_back_keyboard())


@router.message(F.text == BUTTON_HUMIDITY, AuthFilter())
async def button_change_humidity(message: Message, state: FSMContext):
    await state.set_state(ModelStates.PENDING_HUMIDITY)
    await message.answer(MESSAGE_PENDING_MODEL, reply_markup=get_back_keyboard())


@router.message(ModelStates.PENDING_LIGHTING, LightFilter())
async def pending_lighting(message: Message, state: FSMContext):
    change_references(get_key(message.from_user.id), light=int(message.text))
    await message.answer(MESSAGE_LIGHTING.format(message.text))
    await command_model(message, state)


@router.message(ModelStates.PENDING_TEMPERATURE, TempFilter())
async def pending_temperature(message: Message, state: FSMContext):
    change_references(get_key(message.from_user.id), temp=int(message.text))
    await message.answer(MESSAGE_TEMPERATURE.format(message.text))
    await command_model(message, state)


@router.message(ModelStates.PENDING_HUMIDITY, HumidityFilter())
async def pending_humidity(message: Message, state: FSMContext):
    change_references(get_key(message.from_user.id), humidity=int(message.text))
    await message.answer(MESSAGE_HUMIDITY.format(message.text))
    await command_model(message, state)
