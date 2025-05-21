from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Dummy logic for now
    score = 0.6 if data["momentumScore"] > 85 else 0.3
    prediction = 1 if score > 0.5 else 0

    return jsonify({
        "prediction": prediction,
        "confidence": score
    })

if __name__ == "__main__":
    app.run(port=5051)
