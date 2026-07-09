import pandas as pd
from pathlib import Path

def reduce_dataset():
    input_path = Path('data/interim/jobs_clean.csv')
    
    if not input_path.exists():
        print(f"File not found at {input_path}")
        return

    print("Loading 1L+ dataset...")
    df = pd.read_csv(input_path)
    
    # STRATEGY 1: Pure Random Sampling 
    # Grab a random 15,000 rows to keep a diverse mix of jobs.
    df_reduced = df.sample(n=10000, random_state=42)

    # STRATEGY 2: Geographic Filtering (Optional)
    # If you want to tailor the portal for local tech hubs, filter by specific cities.
    # target_cities = ['Visakhapatnam', 'Hyderabad', 'Bangalore', 'Pune']
    # pattern = '|'.join(target_cities)
    # df_reduced = df[df['location'].str.contains(pattern, case=False, na=False)]

    # STRATEGY 3: Domain Filtering (Optional)
    # To make the recommendations highly relevant for a software development student, 
    # filter out non-tech roles (like healthcare or retail).
    # tech_keywords = 'developer|engineer|software|data|react|python'
    # df_reduced = df[df['title'].str.contains(tech_keywords, case=False, na=False)]

    # Save it by overwriting the old file (or save as a new name)
    # Save it as a NEW file to avoid permission locks and preserve the original
    output_path = Path('data/interim/jobs_reduced.csv')
    df_reduced.to_csv(output_path, index=False)
    
    print(f"Dataset successfully reduced to {len(df_reduced)} rows.")

if __name__ == "__main__":
    reduce_dataset()