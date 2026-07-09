import pandas as pd
import re
from pathlib import Path

def generate_skills_column():
    path = Path('data/interim/jobs_reduced.csv')
    df = pd.read_csv(path)
    
    # A master list of common tech skills to hunt for. 
    # Feel free to add more specific skills you want the model to recognize!
    skill_bank = [
        'python', 'java', 'c++', 'c#', 'javascript', 'react', 'node', 'sql', 'mysql', 
        'postgresql', 'mongodb', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 
        'agile', 'linux', 'machine learning', 'ai', 'html', 'css', 'django', 'flask', 
        'spring', 'ruby', 'php', 'typescript', 'hadoop', 'spark', 'pandas', 'tensorflow'
    ]
    
    print("Scanning job descriptions for skills...")
    
    def find_skills(text):
        if not isinstance(text, str): return ""
        text = text.lower()
        # Uses regex boundary \b to ensure we match whole words (e.g., 'c' won't match 'cat')
        found = [skill for skill in skill_bank if re.search(r'\b' + re.escape(skill) + r'\b', text)]
        return " ".join(found)

    # We pull from 'description' first, but fall back to 'title' if it's missing
    text_source = df['description'] if 'description' in df.columns else df['title']
    
    # Create the new skills column
    df['skills'] = text_source.apply(find_skills)
    
    # Save the dataset, overwriting it with the new column included
    df.to_csv(path, index=False)
    print(f"Success! Extracted skills for {len(df)} jobs and saved the file.")

if __name__ == "__main__": 
    generate_skills_column()