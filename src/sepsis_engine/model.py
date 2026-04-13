def predict_sepsis_score(heart_rate: float, temperature: float) -> float:
    """
    Simulates an AI model returning a risk score between 0 and 1.
    High HR and Temp result in a higher risk score.
    """
    # Simple normalized calculation for demonstration
    score = (heart_rate / 200) * 0.5 + (temperature / 42) * 0.5
    return round(min(score, 1.0), 2)
