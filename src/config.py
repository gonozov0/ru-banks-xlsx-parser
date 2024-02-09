from pydantic_settings import BaseSettings


class Config(BaseSettings):
    SERVICE_ACCOUNT_FILE: str | None = None
    SPREADSHEET_ID: str = "1fExaP4qp64vZsoGyN1Fx7l8IznGkl-13AkEczeepW5c"
    SHEET_NAME: str = "Транзакции"
    SCOPES: list = ["https://www.googleapis.com/auth/spreadsheets"]
    TOCHKA_FILE_NAME: str | None = None
    TINKOFF_FILE_NAME: str | None = None
    SBER_INCOME_FILE_NAME: str | None = None
    SBER_OUTCOME_FILE_NAME: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
