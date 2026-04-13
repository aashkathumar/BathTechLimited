from flask import Flask, jsonify
from sepsis_engine.model import predict_sepsis_score
from alert_logic.alerts import generate_alert

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/predict")
def predict():
    score = predict_sepsis_score(110, 39)
    alert = generate_alert(score)

    return jsonify({"score": score, "alert": alert})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
