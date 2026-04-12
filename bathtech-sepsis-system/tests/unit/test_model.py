from src.sepsis_engine.model import predict_sepsis_score

def test_high_risk():
    assert predict_sepsis_score(110, 39) == 2

def test_low_risk():
    assert predict_sepsis_score(80, 36) == 0