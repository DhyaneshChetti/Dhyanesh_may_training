import pickle
from sklearn.cluster import KMeans
from src.config import DATA_PRO, MODELS_DIR

def train_clusters(vecs, df):
    km = KMeans(n_clusters=10, random_state=42, n_init=10).fit(vecs)
    df['cluster'] = km.labels_
    pickle.dump(km, open(MODELS_DIR / 'kmeans.pkl', 'wb'))
    df.to_csv(DATA_PRO / 'clustered_jobs.csv', index=False)
    print(f"Clustering complete. Saved to {DATA_PRO / 'clustered_jobs.csv'}")

def get_market_topics():
    mod = pickle.load(open(MODELS_DIR / 'recommender.pkl', 'rb'))
    words = mod['tfidf'].get_feature_names_out()
    topics = {}
    for i, topic in enumerate(mod['nmf'].components_):
        topics[f"Theme {i+1}"] = [words[i] for i in topic.argsort()[:-6:-1]]
    return topics