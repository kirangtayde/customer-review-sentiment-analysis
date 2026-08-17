from src.text_cleaning import clean_text

def test_clean_text():
    assert clean_text('<b>Great!</b> https://example.com') == 'great'
