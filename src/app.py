from flask import Flask, jsonify
from alert_logic.alerts import generate_alert
# Ensure no trailing spaces on these lines
from sepsis_engine.model import predict_sepsis_score 

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/predict")
def predict():
    hr, temp = 110, 39.0
    is_sepsis = generate_alert(hr, temp)
    
    return jsonify({
        "heart_rate": hr,
        "temperature": temp,
        "sepsis_alert": is_sepsis
    })


# <--- Two blank lines here before the block below
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
# <--- One blank line here at the very end