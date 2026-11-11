from math import ceil


def calculate_price(
    company_type: str,
    tax: str,
    activity: str,
    employees: int,
    operations: int,
    patent: bool = False,
    vat_usn: bool = False,
) -> int:
    base = 0
    included_operations = 0
    included_employees = 0

    if company_type == "ИП без сотрудников":
        base = 5000
        included_operations = 30
        included_employees = 0

    elif company_type == "ИП с сотрудниками":
        base = 11000
        included_operations = 70
        included_employees = 3

    elif company_type == "ООО":
        base = 23000
        included_operations = 150
        included_employees = 5

    if tax == "УСН 15%":
        base += 1000

    elif tax == "ОСНО":
        base += 3000

    if patent:
        base += 2500

    if operations > included_operations:
        base += (operations - included_operations) * 45

    if employees > included_employees:
        base += (employees - included_employees) * 1500

    if activity == "Строительство / Производство":
        base *= 1.2

    if vat_usn:
        base *= 1.2

    return round(base)