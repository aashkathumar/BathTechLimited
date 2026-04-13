from flask import Flask, jsonify
from alert_logic.alerts import generate_alert

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/predict")
def predict():
    # Example logic: in a real system, these would come from patient sensors
    hr, temp = 110, 39.0
    is_sepsis = generate_alert(hr, temp)
    return jsonify({"sepsis_alert": is_sepsis})


# <--- MUST HAVE TWO BLANK LINES HERE
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)