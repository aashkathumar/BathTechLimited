from alert_logic.alerts import generate_alert

def test_sepsis_detected():
    # HR > 90 and Temp > 38.3
    assert generate_alert(heart_rate=110, temperature=39.5) is True

def test_normal_vitals():
    # HR < 90 and Temp < 38.3
    assert generate_alert(heart_rate=70, temperature=37.0) is False

def test_high_hr_only():
    # Should be False if only one criteria is met
    assert generate_alert(heart_rate=100, temperature=37.0) is False