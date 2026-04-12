def generate_alert(score):
    """
    Generates alert based on sepsis score.
    """
    if score >= 2:
        return "HIGH RISK: Immediate attention required"
    elif score == 1:
        return "MEDIUM RISK: Monitor patient"
    return "LOW RISK"