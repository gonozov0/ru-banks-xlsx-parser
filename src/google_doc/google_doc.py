import logging
from datetime import datetime
from typing import Any

from src import dto
from src.google_doc import categories


logger = logging.getLogger(__name__)


def _serialize_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M")


class Sheet:
    def __init__(self, service: Any, spreadsheet_id: str, sheet_name: str):
        self.service = service
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.income_raw = 5
        self.outcome_raw = 5

    def _get_income_range(self) -> str:
        return f"{self.sheet_name}!G{self.income_raw}"

    def _get_outcome_range(self) -> str:
        return f"{self.sheet_name}!B{self.outcome_raw}"

    async def _insert_income(self, data: list[dto.IncomeOperation]):
        body = {
            "values": [
                [
                    _serialize_datetime(op.date),
                    op.amount,
                    op.description,
                    categories.get_income(op.description).value,
                ]
                for op in data
            ]
        }
        result = (
            self.service.spreadsheets()
            .values()
            .update(
                spreadsheetId=self.spreadsheet_id,
                range=self._get_income_range(),
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        self.income_raw += len(data)
        logger.debug("%s income cells updated.", result.get("updatedCells"))

    async def _insert_outcome(self, data: list[dto.OutcomeOperation]):
        body = {
            "values": [
                [
                    _serialize_datetime(op.date),
                    op.amount,
                    op.description,
                    categories.get_outcome(op.description, op.amount).value,
                ]
                for op in data
            ]
        }
        result = (
            self.service.spreadsheets()
            .values()
            .update(
                spreadsheetId=self.spreadsheet_id,
                range=self._get_outcome_range(),
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        self.outcome_raw += len(data)
        logger.debug("%s outcome cells updated.", result.get("updatedCells"))

    async def insert_operations(self, data: dto.Operations):
        await self._insert_income(data=data.incomes)
        await self._insert_outcome(data=data.outcomes)
