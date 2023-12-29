from aiogram.fsm.state import State, StatesGroup


class AuthStates(StatesGroup):
    PENDING_AUTH = State()


class MenuStates(StatesGroup):
    IN_MAIN_MENU = State()
    IN_MODEL_MENU = State()


class ModelStates(StatesGroup):
    PENDING_LIGHTING = State()
    PENDING_TEMPERATURE = State()
    PENDING_HUMIDITY = State()
