import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
from src.models.clustering import train_clusters
from src.config import DATA_INT, DATA_PRO, MODELS_DIR

def build_models():
    df = pd.read_csv(DATA_INT / 'jobs_reduced.csv')
    text = (df['title'] + " " + df['skills'] + " " + df['description']).fillna('')
    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    vecs = tfidf.fit_transform(text)
    pickle.dump({'tfidf': tfidf, 'vecs': vecs}, open(MODELS_DIR / 'recommender.pkl', 'wb'))
    train_clusters(vecs, df)
    nmf = NMF(n_components=5, random_state=42).fit(vecs)
    pickle.dump({'tfidf': tfidf, 'vecs': vecs, 'nmf': nmf}, open(MODELS_DIR / 'recommender.pkl', 'wb'))
    df.to_csv(DATA_PRO / 'clustered_jobs.csv', index=False)

def recommend(resume_text, top_n=5):
    df = pd.read_csv(DATA_PRO / 'clustered_jobs.csv')
    mod = pickle.load(open(MODELS_DIR / 'recommender.pkl', 'rb'))
    sims = cosine_similarity(mod['tfidf'].transform([resume_text]), mod['vecs']).flatten()
    top_idx = sims.argsort()[-top_n:][::-1]
    res = df.iloc[top_idx].copy()
    res['sim_score'] = sims[top_idx]
    return res[['title', 'company', 'location', 'sim_score']], res['cluster'].iloc[0]

if __name__ == "__main__": build_models()