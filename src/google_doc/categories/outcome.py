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
    "VV 7206",
    "VV 6900",
    "VV 6903",
    "WeWork Якиманка",
    "Красное и белое",
    "ВкусВилл",
    "SHAVA - MAMA",
    "SAMOKAT",
    "WeWork Якиманка",
    "PAPA JOHNS",
    "PEREKRESTOK AURA",
    "LLC TRAVEL RETAIL SVO",
    "PYATEROCHKA",
    "IP SHAGIEVA I.I.,UNIVER., 7,INNOPOLIS,RU",
    "MAGNIT",
    "VERNYJ",
    "MATRIKS FUD",
    "KM PROSTAYA EDA K-5",
    "Tyubetey kafe",
    "BRISTOL",
    "KRASNOE BELOE",
    "O ESKIMO",
    "DODO PIZZA",
    "VINLAB",
    "Верный",
    "Пятёрочка",
    "LENTA",
    "Магнит",
    "Tvoya Territoriya..",
    "Столовая ИрНИТУ",
    "Самокат",
    "Трдельник",
    "Кафе",
    "Яндекс Лавка",
    "Перекрёсток",
    "SPAR",
    "Пекарня Хлебница",
]
_gifts_words = [
    "CVETY-BUKETY",
    "GOLD APPLE",
    "PODARKI",
    "EKATERINBURG YABLOKO",
    "Parfum Oil",
    "Konfety Shokolad Suven",
    "Кондитерское производство «Метрополь»",
    "Lavka Vkusnostej",
]
_health_words = [
    "Apteka",
    "APTEKA",
    "OOO MEDAS-MOSKVA",
    "MENTOR-MIND",
    "MANELI",
    "biochek.ru",
    "Аптека",
    "Аптека «Апрель»",
]
_household_words = [
    "PAY.MTS.RU",
    "MAGNIT MK",
    "СВС-Телеком",
    "MosOblEIRC_EPR_1864",
    "OOO RPK 2",
    "Lotos",
    "Мой телефон +7 915 998-65-73",
    "ROSTELECOM.RU",
    "GOSUSLUGI.RU",
    "tome",  # vpn hidemy.name
    "Магнит Косметик",
    "Ростелеком",
    "МосОблЕИРЦ",
]
_transport_words = [
    "Yandex.Fuel",
    "RZD",
    "RZHD",
    "MOSKVA METRO",
    "MOS.TRANSPORT",
    "CITYDRIVE",
    "Payture*YANDEX GO",
    "YANDEX.TAXI",
    "YM *taxi",
    "YM*taxi",
    "YM *Drive",
    "Y.M*DRIVE",
    "KOMSOMOLSKAYA,KOMSOMOLSKAYA SQ,2",
    "URENT",
    "Urentbike",
    "Y.M*GO SCOOTER",
    "YM*GO SCOOTER",
    "KAZANMETRO.RU",
    "DELIMOBIL",
    "Ситидрайв",
    "Яндекс.Заправки",
    "Яндекс.Драйв",
    "Московский метрополитен",
    "Whoosh",
    "Самокаты - Яндекс Go",
    "Делимобиль",
    "Яндекс Такси",
    "Яндекс Драйв",
    "РЖД",
    "Яндекс Заправки",
    "Юрент",
    "Метро Санкт-Петербург",
    "Московский транспорт",
    "Самокаты - Яндекс Go",
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
    "BIRMARKET",
    "YM*PLUS",
    "COFFEEWAY",
    "Tangiers Lounge",
    "TANGIERS LOUNGE",
    "HOOKAHPLACE",
    "COFFEE CAVA",
    "COFFE CAVA",
    "COFFEEIN",
    "KSTB",
    "OOO MEMSOL",
    "LAUNZH BAR",
    "BUDDU LOUNGE",
    "netmonet,UL SOLNECHNAYA,DOM 7, OFI,VORONEZH,RU",
    "booble mania",
    "COFFEE TIME",
    "Hookah Place",
    "HOOKAPLACE",
    "E-GO KARTING",
    "SYROVARNYA",
    "DABLBI",
    "COFFEE GALLERY",
    "COFIX",
    "JACKY JACKY LIFE",
    "RESTORAN FINIST",
    "Kofeynya",
    "Hookan Place",
    "FRANK by БАСТА",
    "Шоколадница",
    "Dune",
    "Moo Moo Burgers",
    "Буше",
    "Kafe Tayyaki",
    "Medved",
    "ЦЕХ 85",
    "Pantao Asian Bar",
    "Skuratov Сoffee",
    "Taverna Sirtaki",
    "Ramen Rebel",
    "RBE Group",
    "Моремания",
    "#FARШ",
    "Кофейня",
    "Московская Кофейная Сеть",
]
_investments_words = []
_travel_words = [
    "OOO POBEDA",
    "FLYSMARTAVIA",
    "KAZAN KREMLIN",
    "PARKOMAT 1,STR PRIBREZHNAYA 2,SAVINO",
    "MUZEJ",
    "SUVENIR",
    "MUZEY",
    "Яндекс.Путешествия",
    "Аэрофлот",
    "ИНДИВИДУАЛЬНЫЙ ПРЕДПРИНИМАТЕЛЬ БРЕМОВ БРЕМ АБДУКЕРИМОВИЧ",
    "Выборгский объединенный музей-заповедник",
    "Музей истории Санкт-Петербурга",
    "Казанский кафедральный собор",
]
_beauty_words = [
    "Достонбек Н.",
    "IP PARSEGOVA LR,sh Nosovikhinskoye",
    "OOO ESTETIKA",
    "Черная кость Юбилейный пр-т",
]
_education_words = [
    "BOOSTY",
    "smart-glocal",
    "YANDEX.CLOUD",
    "SMART GLOCAL",
    "Boosty.to",
]
_trainers = [
    ("Антон Ч.", 40000),
    ("Андрей П.", 48000),
    ("Андрей П.", 16000)
]
_sports_words = [
    "FITNESS HOUSE",
    "ALFA DZHIM",
    "OOO MEGASPORT",
]
_clothing_words = [
    "LAMODA",
    "FAMILIA",
    "OSTIN",
]
_ozone_words = [
    "OZON",
    "WILDBERRIES",
    "Y.M*MARKET.YANDEX",
    "Aliexpress",
    "Яндекс Маркет",
]
_taxes_words = [
    "Единый налоговый платеж",
    "GOSUSLUGI SHTRAFY",
    "Федеральная Налоговая Служба",
]
_cat_words = [
    "SP DOBRYJ DOKTOR",
    "ZOOMAGAZIN",
    "Четыре Лапы",
]


def get_outcome(description: str, amount: float) -> OutcomeCategory:
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
    for sub_desc, amount_ in _trainers:
        if amount_ == amount and sub_desc in description:
            return OutcomeCategory.Sports
    if shared.is_found(description, _clothing_words):
        return OutcomeCategory.Clothing
    if shared.is_found(description, _ozone_words):
        return OutcomeCategory.Ozone
    if shared.is_found(description, _taxes_words):
        return OutcomeCategory.Taxes
    if shared.is_found(description, _cat_words):
        return OutcomeCategory.Cat

    if amount in (50, 100):
        return OutcomeCategory.Transport
    if amount == 92776:
        return OutcomeCategory.Mortgage

    return OutcomeCategory.Other
