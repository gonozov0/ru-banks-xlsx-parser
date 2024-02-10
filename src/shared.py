from pathlib import Path


class FileNotFound(Exception):
    pass


def find_latest_file_name(dir_path: str) -> str:
    full_path = Path(dir_path).resolve()
    latest_file_name = None
    latest_mod_time = 0

    for item in full_path.iterdir():
        if not item.is_file() or item.name == ".gitkeep":
            continue
        mod_time = item.stat().st_mtime
        if mod_time <= latest_mod_time:
            continue
        latest_mod_time = mod_time
        latest_file_name = item.name

    if not latest_file_name:
        raise FileNotFound(f"No files found in {dir_path}")

    return latest_file_name
