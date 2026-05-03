from app.text_analyzer import analyze_text


def test_analyze_text_counts_characters():
    result = analyze_text("hello")
    assert result["characters"] == 5


def test_analyze_text_counts_words():
    result = analyze_text("one two three")
    assert result["words"] == 3


def test_analyze_text_counts_sentences():
    result = analyze_text("First. Second. Third.")
    assert result["sentences"] == 3


def test_analyze_text_handles_empty_text():
    result = analyze_text("")
    assert result["characters"] == 0
    assert result["words"] == 0
    assert result["sentences"] == 0
