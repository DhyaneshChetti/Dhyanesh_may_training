import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.config import DATA_RAW, MODELS_DIR
from src.features.text_features import clean_text

def train():
    df = pd.read_csv(DATA_RAW / 'resumes_clean.csv')
    df['clean'] = clean_text(df['text'])
    
    tfidf = TfidfVectorizer(max_features=3000, stop_words='english')
    X = tfidf.fit_transform(df['clean'])
    clf = LogisticRegression(max_iter=1000).fit(X, df['Category'])
    
    MODELS_DIR.mkdir(exist_ok=True)
    pickle.dump(tfidf, open(MODELS_DIR / 'tfidf_vectorizer.pkl', 'wb'))
    pickle.dump(clf, open(MODELS_DIR / 'classifier.pkl', 'wb'))

if __name__ == "__main__": train()