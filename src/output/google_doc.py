import logging
from datetime import datetime
from typing import Any

from src import dto


logger = logging.getLogger(__name__)


def _serialize_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


class Sheet:
    def __init__(self, service: Any, spreadsheet_id: str, sheet_name: str):
        self.service = service
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.start_income_raw = 5
        self.start_outcome_raw = 5

    def _get_income_range(self) -> str:
        return f"{self.sheet_name}!G{self.start_income_raw}"

    def _get_outcome_range(self) -> str:
        return f"{self.sheet_name}!B{self.start_outcome_raw}"

    async def _insert_income(self, data: list[dto.IncomeOperation]):
        body = {"values": [[_serialize_datetime(op.date), op.amount, op.description] for op in data]}
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
        logger.info("%s income cells updated.", result.get("updatedCells"))

    async def _insert_outcome(self, data: list[dto.OutcomeOperation]):
        body = {"values": [[_serialize_datetime(op.date), op.amount, op.description] for op in data]}
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
        logger.info("%s outcome cells updated.", result.get("updatedCells"))

    async def insert_operations(self, data: dto.Operations):
        await self._insert_income(data=data.incomes)
        await self._insert_outcome(data=data.outcomes)
