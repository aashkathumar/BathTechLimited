def predict_sepsis_score(heart_rate, temperature):
    """
    Simple rule-based sepsis score.
    """
    score = 0

    if heart_rate > 100:
        score += 1
    if temperature > 38:
        score += 1

    return score
