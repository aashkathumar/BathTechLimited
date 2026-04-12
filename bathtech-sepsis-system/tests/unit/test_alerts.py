from src.alert_logic.alerts import generate_alert

def test_high_alert():
    assert "HIGH" in generate_alert(2)

def test_low_alert():
    assert "LOW" in generate_alert(0)