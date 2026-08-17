from __future__ import annotations
import re

def clean_text(text: str) -> str:
    text=str(text).lower()
    text=re.sub(r'<[^>]+>',' ',text)
    text=re.sub(r'https?://\S+|www\.\S+',' ',text)
    text=re.sub(r'[^a-z\s]',' ',text)
    return re.sub(r'\s+',' ',text).strip()

def normalize_reviews(texts): return [clean_text(x) for x in texts]
