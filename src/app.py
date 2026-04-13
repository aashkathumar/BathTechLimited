from flask import Flask, jsonify
# These imports now match the folder structure
from alert_logic.alerts import generate_alert 
from sepsis_engine.model import predict_sepsis_score 

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/predict")
def predict():
    # Example values for your scoring engine
    score = predict_sepsis_score(110, 39)
    alert = generate_alert(score)
    return jsonify({"score": score, "alert": alert})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)