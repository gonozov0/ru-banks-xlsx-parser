from enum import Enum

from src.google_doc.categories import shared


class OutcomeCategory(Enum):
    Food = "Питание"
    Gifts = "Подарки"
    Health = "Здоровье/медицина"
    Household = "Дом/быт"
    Transport = "Транспорт"
    Entertainment = "Развлечения"
    Investments = "Инвестиции"
    Travel = "Путешествия"
    Beauty = "Красота"
    Education = "Образование"
    Sports = "Спорт"
    Clothing = "Одежда"
    Ozone = "Озон"
    Taxes = "Налоги"
    Mortgage = "Ипотека"
    Cat = "Кошка"
    Other = "Другое"


_food_words = [
    "VKUSVILL",
    "KRASNOE I BELOE",
    "VV 6344",
    "WeWork Якиманка",
    "Красное и белое",
    "ВкусВилл",
    "SHAVA - MAMA",
]
_gifts_words = []
_health_words = [
    "Apteka",
    "APTEKA",
    "OOO MEDAS-MOSKVA",
    "MENTOR-MIND",
    "MANELI",
]
_household_words = [
    "PAY.MTS.RU",
    "MAGNIT MK",
    "СВС-Телеком",
    "MosOblEIRC_EPR_1864",
]
_transport_words = [
    "Yandex.Fuel",
    "Payture*YANDEX GO",
    "RZD",
    "RZHD",
    "MOSKVA METRO",
    "MOS.TRANSPORT",
    "CITYDRIVE",
    "YANDEX.TAXI",
    "YM *Drive",
]
_entertainment_words = [
    "ONEPRICE",
    "ONE PRICE COFFEE",
    "HAPPY COFFEE",
    "VESELAYA ZATEYA",
    "MYATA SIGNATURE",
    "BOONCAKE.CAFE",
    "Steamstar",
    "hardparty",
    "SAD Lounge",
    "TAYSPA",
    "YANDEX.EDA",
    "SMOKE PISTOLS GANG",
    "AYN BAR",
    "DUNE,PR-T YUBILEYNYY",
]
_investments_words = []
_travel_words = []
_beauty_words = [
    "Достонбек Н.",
    "IP PARSEGOVA LR,sh Nosovikhinskoye",
]
_education_words = [
    "BOOSTY",
    "smart-glocal",
    "YANDEX.CLOUD",
]
_sports_words = []
_clothing_words = [
    "LAMODA",
]
_ozone_words = [
    "OZON",
    "WILDBERRIES",
    "Y.M*MARKET.YANDEX",
    "Aliexpress",
]
_taxes_words = [
    "Единый налоговый платеж",
]
_cat_words = [
    "SP DOBRYJ DOKTOR",
    "ZOOMAGAZIN",
]


def get_outcome(description: str, amount: float) -> OutcomeCategory:
    if amount in (45, 50, 90, 100):
        return OutcomeCategory.Transport
    if amount == 92776:
        return OutcomeCategory.Mortgage

    if shared.is_found(description, _food_words):
        return OutcomeCategory.Food
    if shared.is_found(description, _gifts_words):
        return OutcomeCategory.Gifts
    if shared.is_found(description, _health_words):
        return OutcomeCategory.Health
    if shared.is_found(description, _household_words):
        return OutcomeCategory.Household
    if shared.is_found(description, _transport_words):
        return OutcomeCategory.Transport
    if shared.is_found(description, _entertainment_words):
        return OutcomeCategory.Entertainment
    if shared.is_found(description, _investments_words):
        return OutcomeCategory.Investments
    if shared.is_found(description, _travel_words):
        return OutcomeCategory.Travel
    if shared.is_found(description, _beauty_words):
        return OutcomeCategory.Beauty
    if shared.is_found(description, _education_words):
        return OutcomeCategory.Education
    if shared.is_found(description, _sports_words):
        return OutcomeCategory.Sports
    if shared.is_found(description, _clothing_words):
        return OutcomeCategory.Clothing
    if shared.is_found(description, _ozone_words):
        return OutcomeCategory.Ozone
    if shared.is_found(description, _taxes_words):
        return OutcomeCategory.Taxes

    return OutcomeCategory.Other
