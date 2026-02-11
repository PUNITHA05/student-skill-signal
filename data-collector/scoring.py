def calculate_skill_score(repo_count, language_count):

   
    if repo_count >= 7:
        repo_score = 1
    elif repo_count >= 3:
        repo_score = 0.6
    else:
        repo_score = 0.3

    
    if language_count >= 4:
        language_score = 1
    elif language_count >= 2:
        language_score = 0.6
    else:
        language_score = 0.3

    
    if repo_count >= 5:
        activity_score = 1
    else:
        activity_score = 0.5

    final_score = (
        repo_score * 40 +
        language_score * 30 +
        activity_score * 30
    )

    return repo_score, language_score, activity_score, final_score
