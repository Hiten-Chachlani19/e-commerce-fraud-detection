from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app) # Enables Frontend-Backend Cross Origin communication

# Load trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/fraud_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "running", "message": "E-Commerce Fraud Detection API Active"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features from request payload
        features = [
            float(data['transaction_amount']),
            int(data['transaction_hour']),
            float(data['distance_from_home_km']),
            int(data['failed_login_attempts']),
            int(data['is_foreign_ip']),
            int(data['is_high_risk_country']),
            int(data['shipping_billing_address_match']),
            int(data['device_type'])
        ]
        
        # Prediction & Probability Calculation
        input_data = np.array([features])
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        fraud_probability = round(float(probabilities[1]) * 100, 2)
        
        return jsonify({
            'is_fraud': int(prediction),
            'fraud_probability': fraud_probability,
            'status': 'HIGH RISK - FRAUD DETECTED' if prediction == 1 else 'LOW RISK - SAFE TRANSACTION'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)