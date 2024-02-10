def is_found(description: str, words: list[str]) -> bool:
    for word in words:
        if word in description:
            return True
    return False
