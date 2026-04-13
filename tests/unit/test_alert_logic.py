from alert_logic import check_sepsis


def test_normal_patient_no_sepsis():
    assert not check_sepsis(heart_rate=72, temperature=37.0)


def test_sepsis_detected():
    assert check_sepsis(heart_rate=110, temperature=39.1)


def test_high_hr_normal_temp_no_sepsis():
    assert not check_sepsis(heart_rate=95, temperature=37.5)
    