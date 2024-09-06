import asyncio
import logging

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from src import banks, creds, google_doc, transfer
from src.config import Config


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


async def main():
    config = Config()
    credentials = Credentials.from_service_account_file(
        filename=creds.get_path(file_name=config.SERVICE_ACCOUNT_FILE),
        scopes=config.SCOPES,
    )
    service = build(serviceName="sheets", version="v4", credentials=credentials)

    # tochka = banks.Tochka(dir_path=config.TOCHKA_DIR_PATH, file_name=config.TOCHKA_FILE_NAME)
    tinkoff = banks.Tinkoff(dir_path=config.TINKOFF_DIR_PATH, file_name=config.TINKOFF_FILE_NAME)
    sber = banks.Sber(
        income_dir_path=config.SBER_INCOME_DIR_PATH,
        income_file_name=config.SBER_INCOME_FILE_NAME,
        outcome_dir_path=config.SBER_OUTCOME_DIR_PATH,
        outcome_file_name=config.SBER_OUTCOME_FILE_NAME,
    )
    google_sheet = google_doc.Sheet(
        service=service,
        spreadsheet_id=config.SPREADSHEET_ID,
        sheet_name=config.SHEET_NAME,
    )

    await transfer.transfer_banks(banks_=[tinkoff, sber], sheet=google_sheet)


if __name__ == "__main__":
    asyncio.run(main())
