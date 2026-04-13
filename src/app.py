from flask import Flask, jsonify
from alert_logic.alerts import generate_alert
from sepsis_engine.model import predict_sepsis_score

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/predict")
def predict():
    hr, temp = 110, 39.0
    # Using the import to fix the F401 error
    score = predict_sepsis_score(hr, temp)
    is_sepsis = generate_alert(hr, temp)
    return jsonify({
        "sepsis_alert": is_sepsis,
        "risk_score": score
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
