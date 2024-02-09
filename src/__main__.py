import asyncio
import logging

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from src import paths
from src.config import Config
from src.input import tochka
from src.output import google_doc


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


async def main():
    config = Config()
    logger.info(paths.get_creds(file_name=config.SERVICE_ACCOUNT_FILE))
    creds = Credentials.from_service_account_file(
        filename=paths.get_creds(file_name=config.SERVICE_ACCOUNT_FILE),
        scopes=config.SCOPES,
    )
    service = build(serviceName="sheets", version="v4", credentials=creds)

    tochka_operations = await tochka.get_operations(paths.get_tochka(file_name=config.TOCHKA_FILE_NAME))

    google_sheet = google_doc.Sheet(
        service=service,
        spreadsheet_id=config.SPREADSHEET_ID,
        sheet_name=config.SHEET_NAME,
    )
    await google_sheet.insert_operations(tochka_operations)


if __name__ == "__main__":
    asyncio.run(main())
