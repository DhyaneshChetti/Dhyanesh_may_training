import re
from collections import Counter

def get_skill_gap(resume_text, target_skills_text):
    skill_bank = [
        'python', 'java', 'c++', 'c#', 'javascript', 'react', 'node', 'sql', 'mysql', 
        'postgresql', 'mongodb', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 
        'agile', 'linux', 'machine learning', 'ai', 'html', 'css', 'django', 'flask', 
        'spring', 'ruby', 'php', 'typescript', 'hadoop', 'spark', 'pandas', 'tensorflow'
    ]
    target_words = target_skills_text.lower().split()
    valid_target_skills = [w for w in target_words if w in skill_bank]
    top_role_skills = [skill for skill, count in Counter(valid_target_skills).most_common(15)] 
    resume_lower = resume_text.lower()
    resume_skills = [skill for skill in skill_bank if re.search(r'\b' + re.escape(skill) + r'\b', resume_lower)]
    gaps = [skill for skill in top_role_skills if skill not in resume_skills]
    
    return gaps[:10]