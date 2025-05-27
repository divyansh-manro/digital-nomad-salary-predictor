from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('nomad_salary_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_salary():
    try:
        # Get JSON data
        data = request.json
        
        # Validate required fields
        required_fields = [
            'job_role', 'company_remote', 'location',
            'nomad_visa', 'productivity', 'burnout_level'
        ]
        
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Prepare input data
        input_data = {
            'job_role': data['job_role'],
            'company_remote': 1 if str(data['company_remote']).upper() == 'Y' else 0,
            'location': data['location'],
            'nomad_visa': 1 if str(data['nomad_visa']).upper() == 'Y' else 0,
            'productivity': int(data['productivity']),
            'burnout_level': int(data['burnout_level']),
            'city': data['location'].split(',')[0].strip(),
            'country': data['location'].split(',')[1].strip()
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Make prediction
        prediction = model.predict(input_df)
        
        return jsonify({
            'predicted_salary_usd': round(float(prediction[0]), 2),
            'input_features': input_data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)