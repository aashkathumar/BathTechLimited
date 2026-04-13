import requests
import time

def test_api_health_endpoint():
    # Hits the local server started in the CI pipeline
    response = requests.get("http://localhost:8080/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_api_prediction_endpoint():
    response = requests.get("http://localhost:8080/predict")
    assert response.status_code == 200
    assert "sepsis_alert" in response.json()