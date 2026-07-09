import pandas as pd
import pickle
import sys
from pathlib import Path
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, silhouette_score)
from sklearn.preprocessing import label_binarize
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import DATA_RAW, DATA_PRO, MODELS_DIR
import src.features.text_features
import src.models.recommender

def evaluate_classifier():
    print("\n1. CLASSIFICATION METRICS\n")
    df = pd.read_csv(DATA_RAW / 'resumes_clean.csv')
    
    tfidf = pickle.load(open(MODELS_DIR / 'tfidf_vectorizer.pkl', 'rb'))
    clf = pickle.load(open(MODELS_DIR / 'classifier.pkl', 'rb'))
    
    X = tfidf.transform(src.features.text_features.clean_text(df['text']))
    y_true = df['Category']
    y_pred = clf.predict(X)
    y_prob = clf.predict_proba(X)
    y_bin = label_binarize(y_true, classes=clf.classes_)
    
    print(f"Accuracy:  {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred, average='weighted', zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_true, y_pred, average='weighted', zero_division=0):.4f}")
    print(f"F1-Score:  {f1_score(y_true, y_pred, average='weighted', zero_division=0):.4f}")
    print(f"ROC-AUC:   {roc_auc_score(y_bin, y_prob, average='weighted', multi_class='ovr'):.4f}")
    print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))

def evaluate_clustering():
    print("\n2. CLUSTERING METRICS\n")
    mod = pickle.load(open(MODELS_DIR / 'recommender.pkl', 'rb'))
    km = pickle.load(open(MODELS_DIR / 'kmeans.pkl', 'rb'))
    df = pd.read_csv(DATA_PRO / 'clustered_jobs.csv')
    vecs = mod['vecs']
    labels = df['cluster']
    print(f"Inertia (Elbow Method): {km.inertia_:.2f}")
    print(f"Silhouette Score: {silhouette_score(vecs, labels):.4f}")

def evaluate_recommender():
    print("\n3. RECOMMENDER (Precision@K)\n")
    sample_cv = "Senior Software Engineer. Expert in Python, Django, AWS, and REST APIs."
    print(f"Qualitative Input: '{sample_cv}'\n")
    recs, _ = src.models.recommender.recommend(src.features.text_features.clean_text(sample_cv), top_n=5)
    print(recs[['title', 'sim_score']].to_string(index=False))
    relevant_matches = (recs['sim_score'] > 0.10).sum()
    print(f"\nHeuristic Precision@5: {relevant_matches / 5:.2f} ({relevant_matches}/5 matches relevant)")


if __name__ == "__main__":
    evaluate_classifier()
    evaluate_clustering()
    evaluate_recommender()


