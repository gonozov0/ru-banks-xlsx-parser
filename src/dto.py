from datetime import datetime

from pydantic import BaseModel


class IncomeOperation(BaseModel):
    amount: float
    date: datetime
    description: str


class OutcomeOperation(BaseModel):
    amount: float
    date: datetime
    description: str


class Operations(BaseModel):
    incomes: list[IncomeOperation]
    outcomes: list[OutcomeOperation]
