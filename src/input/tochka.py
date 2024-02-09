import openpyxl

from src import dto


async def get_operations(file_path: str) -> dto.Operations:
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    income_operations = []
    outcome_operations = []

    for row in sheet.iter_rows(min_row=3):  # предполагается, что первая строка - заголовки
        date = row[1].value
        income_amount = row[11].value
        outcome_amount = row[10].value
        description = row[12].value
        if not (date or income_amount or outcome_amount or description):
            break

        if income_amount:
            income_operations.append(
                dto.IncomeOperation(
                    date=date,
                    amount=income_amount,
                    description=description,
                )
            )
        else:
            outcome_operations.append(
                dto.OutcomeOperation(
                    date=date,
                    amount=outcome_amount,
                    description=description,
                )
            )

    return dto.Operations(
        incomes=income_operations,
        outcomes=outcome_operations,
    )
