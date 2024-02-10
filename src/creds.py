from os import path

from src import shared


def get_path(file_name: str | None) -> str:
    dir_path = "creds"
    if not file_name:
        file_name = shared.find_latest_file_name(dir_path)

    return path.join(dir_path, file_name)
