from src.alert_logic import check_sepsis

def test_normal_patient_no_sepsis():
    assert check_sepsis(heart_rate=72, temperature=37.0) == False

def test_sepsis_detected():
    assert check_sepsis(heart_rate=110, temperature=39.1) == True

def test_high_hr_normal_temp_no_sepsis():
    assert check_sepsis(heart_rate=95, temperature=37.5) == False