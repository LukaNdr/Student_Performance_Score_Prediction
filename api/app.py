from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = "model/trained_model.pkl"
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    raise Exception(f"Model file not found at {MODEL_PATH}. Please make sure it exists.")

# Define a route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data as JSON
        data = request.json

        # Extract features from the request
        features = [
            data.get("dailyHoursStudy"),
            data.get("attendance"),
            data.get("resourcesAccess"),
            data.get("extracurricularActivities"),
            data.get("sleepHours"),
            data.get("motivationLevel"),
            data.get("haveAJob"),
            data.get("teacherQuality"),
            data.get("schoolType"),
            data.get("interestForSubject"),
            data.get("distanceFromHome"),
            data.get("selfRatingStudent"),
            data.get("learningLanguage"),
            data.get("numberOfSubjects"),
            data.get("timeSpentSocialMedia"),
            data.get("mentalHealthCondition")
        ]

        # Convert features to a NumPy array (ensure correct format for model input)
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        # Return the result as JSON
        return jsonify({"predictedScore": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)