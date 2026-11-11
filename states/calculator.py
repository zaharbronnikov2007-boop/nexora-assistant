from aiogram.fsm.state import State, StatesGroup


class CalculatorState(StatesGroup):
    business_type = State()
    tax_system = State()
    activity = State()
    employees = State()
    operations = State()
    patent = State()
    vat = State()