def generate_alert(heart_rate: float, temperature: float) -> bool:
    """
    Returns True if patient vitals indicate possible sepsis.
    Criteria: heart rate > 90 bpm AND temperature > 38.3C
    """
    return heart_rate > 90 and temperature > 38.3
