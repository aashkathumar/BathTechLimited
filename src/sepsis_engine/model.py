def predict_sepsis_score(heart_rate: float, temperature: float) -> float:
    """Simulates an AI model returning a risk score."""
    score = (heart_rate / 200) * 0.5 + (temperature / 42) * 0.5
    return round(min(score, 1.0), 2)
