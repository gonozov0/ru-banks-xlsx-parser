from enum import Enum

from src.google_doc.categories import shared


class IncomeCategory(Enum):
    Salary = "Зарплата"
    Cashback = "Кешбэк"
    Interest = "Процентный доход"
    Other = "Прочие пополнения"


_salary_words = [
    "Оплата услуг",
    "Оплата за услуги",
    "Пополнение через Сбербанк",
]
_cashback_words = [
    "Кэшбэк",
]
_interest_words = [
    "Проценты",
    "Капитализация по вкладу/счету",
]


def get_income(description: str) -> IncomeCategory:
    if shared.is_found(description, _salary_words):
        return IncomeCategory.Salary
    if shared.is_found(description, _cashback_words):
        return IncomeCategory.Cashback
    if shared.is_found(description, _interest_words):
        return IncomeCategory.Interest

    return IncomeCategory.Other
