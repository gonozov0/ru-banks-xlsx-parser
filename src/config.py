from pydantic_settings import BaseSettings


class Config(BaseSettings):
    SERVICE_ACCOUNT_FILE: str | None = None
    SPREADSHEET_ID: str = "1Dwiy2OChUR_iToA7YVGtTkH5W8bx3XdK4HeFVpzJMw8"
    SHEET_NAME: str = "Транзакции"
    SCOPES: list = ["https://www.googleapis.com/auth/spreadsheets"]
    TOCHKA_DIR_PATH: str = "data/tochka"
    TOCHKA_FILE_NAME: str | None = None
    TINKOFF_DIR_PATH: str = "data/tinkoff"
    TINKOFF_FILE_NAME: str | None = None
    SBER_INCOME_DIR_PATH: str = "data/sber/income"
    SBER_INCOME_FILE_NAME: str | None = None
    SBER_OUTCOME_DIR_PATH: str = "data/sber/outcome"
    SBER_OUTCOME_FILE_NAME: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
