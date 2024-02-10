from datetime import datetime
from os import path

import xlrd

from src import dto, shared
from src.banks import interface


def _deserialize_date(date: str) -> datetime:
    return datetime.strptime(date, "%d.%m.%Y %H:%M:%S")


_filter_words = [
    "Перевод между счетами",
    "Дмитрий Г.",
]


def _filter(description: str) -> bool:
    for word in _filter_words:
        if word in description:
            return True

    return False


class Tinkoff(interface.IBank):
    def __init__(self, dir_path: str, file_name: str | None):
        if not file_name:
            file_name = shared.find_latest_file_name(dir_path)

        self.file_path = path.join(dir_path, file_name)

    async def get_name(self) -> str:
        return "Tinkoff"

    async def get_operations(self) -> dto.Operations:
        # Открываем книгу используя xlrd
        workbook = xlrd.open_workbook(self.file_path)
        sheet = workbook.sheet_by_index(0)
        income_operations = []
        outcome_operations = []

        for row_idx in range(2, sheet.nrows):
            row = sheet.row(row_idx)
            date = _deserialize_date(row[0].value)
            status = row[3].value
            amount = int(row[4].value)
            description = row[11].value
            if not (date or amount or description):
                break
            if status == "FAILED":
                continue
            if _filter(description):
                continue

            if amount > 0:
                income_operations.append(
                    dto.IncomeOperation(
                        date=date,
                        amount=amount,
                        description=description,
                    )
                )
            else:
                outcome_operations.append(
                    dto.OutcomeOperation(
                        date=date,
                        amount=abs(amount),
                        description=description,
                    )
                )

        return dto.Operations(
            incomes=income_operations,
            outcomes=outcome_operations,
        )
