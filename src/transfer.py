import asyncio
import logging

from src import banks, google_doc


logger = logging.getLogger(__name__)


async def _transfer_bank(bank: banks.IBank, sheet: google_doc.Sheet):
    operations = await bank.get_operations()
    await sheet.insert_operations(operations)
    logger.info(
        "%d income operations from %s have been transferred to Google Sheet.",
        len(operations.incomes),
        await bank.get_name(),
    )
    logger.info(
        "%d outcome operations from %s have been transferred to Google Sheet.",
        len(operations.outcomes),
        await bank.get_name(),
    )


async def transfer_banks(banks_: list[banks.IBank], sheet: google_doc.Sheet):
    tasks = [_transfer_bank(bank, sheet) for bank in banks_]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if not isinstance(result, Exception):
            continue

        logger.error(result)
        raise result
