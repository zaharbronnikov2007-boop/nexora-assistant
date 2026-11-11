from aiogram.fsm.state import State, StatesGroup


class ConsultationState(StatesGroup):
    # Консультация
    name = State()
    business_type = State()
    tax_system = State()
    employees = State()
    service = State()
    description = State()
    phone = State()

    # Калькулятор
    activity = State()
    operations = State()
    patent = State()
    vat = State()