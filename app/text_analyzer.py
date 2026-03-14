def analyze_text(text: str) -> dict:
    """Return character count, word count, and sentence count (by '.')."""
    characters = len(text)
    words = len(text.split()) if text.strip() else 0
    sentences = text.count(".")
    return {
        "characters": characters,
        "words": words,
        "sentences": sentences,
    }
