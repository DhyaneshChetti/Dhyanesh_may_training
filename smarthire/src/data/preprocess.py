import pandas as pd
import os

print("Loading raw datasets...")
naukri_df = pd.read_csv('data/raw/naukri_com-job_sample.csv')
linkedin_df = pd.read_csv('data/raw/indian_tech_jobs_2026.csv')
        
if 'job_title' in linkedin_df.columns:
    linkedin_df = linkedin_df.rename(columns={
        'job_title': 'title',
        'skills_required': 'skills',
        'experience_tier': 'experience',
        'location': 'location',
        'company_name': 'company',
        'job_description': 'description'
    })

if 'jobtitle' in naukri_df.columns:
    naukri_df = naukri_df.rename(columns={
        'jobtitle': 'title',
        'company': 'company',
        'joblocation_address': 'location',
        'skills': 'skills',
        'jobdescription': 'description',
        'experience': 'experience'
    })

common_cols = ['title', 'company', 'location', 'skills', 'description', 'experience']
    
linkedin_clean = linkedin_df[[c for c in common_cols if c in linkedin_df.columns]]
naukri_clean = naukri_df[[c for c in common_cols if c in naukri_df.columns]]
    
merged_corpus = pd.concat([linkedin_clean,naukri_clean], ignore_index=True)
merged_corpus.drop_duplicates(inplace=True)
merged_corpus.fillna('', inplace=True)

output_path = 'data/interim/merged_job_corpus.csv'
merged_corpus.to_csv(output_path, index=False)
print(f"Success! Job corpus built with {len(merged_corpus)} jobs and saved to {output_path}")