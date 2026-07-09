import streamlit as st
import pandas as pd
import pickle, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.recommender import recommend
from src.models.clustering import get_market_topics
from src.models.fit_predictor import calculate_fit_score
from src.parsing.resume_parser import extract_text
from src.features.text_features import clean_text
from src.features.match_features import get_skill_gap
from src.config import DATA_INT, DATA_PRO, MODELS_DIR

st.set_page_config(layout="wide")
st.title("SmartHire ML Engine")

with st.sidebar:
    st.header("Market Insights")
    themes = get_market_topics()
    for theme, words in themes.items():
        st.caption(f"**{theme}**: {', '.join(words).title()}")

file = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])

if st.button("Analyze"):
    if file:
        raw_text = extract_text(file)
        cleaned_text = clean_text(raw_text)

        tfidf = pickle.load(open(MODELS_DIR / 'tfidf_vectorizer.pkl', 'rb'))
        clf = pickle.load(open(MODELS_DIR / 'classifier.pkl', 'rb'))
        predicted_role = clf.predict(tfidf.transform([cleaned_text]))[0]

        df_jobs = pd.read_csv(DATA_INT / 'jobs_reduced.csv')
        role_jobs = df_jobs[df_jobs['title'].str.contains(predicted_role[:4], case=False, na=False)]
        recs, target_cluster = recommend(cleaned_text)
        if role_jobs.empty:
            df_clustered = pd.read_csv(DATA_PRO / 'clustered_jobs.csv')
            role_jobs = df_clustered[df_clustered['cluster'] == target_cluster]

        role_skills_text = " ".join(role_jobs['skills'].fillna('')) 
        gaps = get_skill_gap(raw_text, role_skills_text)
        recs['Fit Score %'] = recs['sim_score'].apply(lambda x: calculate_fit_score(x, len(gaps)))
        recs = recs.drop(columns=['sim_score']).sort_values(by='Fit Score %', ascending=False)
    
        st.success(f"Predicted Role: {predicted_role}")
    
        st.subheader("Top Job Matches (Ranked by Fit Score)")
        st.dataframe(recs, use_container_width=True)
    
        st.subheader(f"Skill Gap Analysis for: {predicted_role}")
        st.info("To improve your chances of selecting for the role , consider learning: " + ", ".join([g.capitalize() for g in gaps]))
    else:
        st.warning("Please upload a resume to see recommendations.")