from summarizer import summarize_text

def test_summary_returns_string():
    result = summarize_text("This is a test.")
    assert isinstance(result, str)
    assert len(result) > 0
