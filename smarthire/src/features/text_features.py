import re
import pandas as pd

def clean_text(text):
    if isinstance(text, pd.Series):
        return text.str.replace(r'http\S+|#\S+|@\S+|[^a-zA-Z\s]', ' ', regex=True).str.lower().str.replace(r'\s+', ' ', regex=True)
    return re.sub(r'\s+', ' ', re.sub(r'http\S+|#\S+|@\S+|[^a-zA-Z\s]', ' ', str(text))).lower().strip()