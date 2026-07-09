def calculate_fit_score(cosine_similarity, num_missing_skills):
    base_score = min(cosine_similarity * 100 * 2.5, 75)
    skill_score = max(0, 25 - (num_missing_skills * 2.5))
    return min(max(round(base_score + skill_score, 1), 0), 100)