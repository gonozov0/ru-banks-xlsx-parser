def is_found(description: str, words: list[str]) -> bool:
    description = description.lower()
    for word in words:
        if word.lower() in description:
            return True
    return False
