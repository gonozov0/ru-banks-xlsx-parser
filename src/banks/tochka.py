from os import path

import openpyxl

from src import dto, shared
from src.banks import interface


_filter_words = [
    "P2P Перевод с карты",
]


def _filter(description: str) -> bool:
    for word in _filter_words:
        if word in description:
            return True
    return False


class Tochka(interface.IBank):
    def __init__(self, dir_path: str, file_name: str | None):
        if not file_name:
            file_name = shared.find_latest_file_name(dir_path)

        self.file_path = path.join(dir_path, file_name)

    async def get_name(self) -> str:
        return "Tochka"

    async def get_operations(self) -> dto.Operations:
        workbook = openpyxl.load_workbook(self.file_path)
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
            if _filter(description):
                continue

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
