Titanic Fare Prediction API Documentation
Introduction
This project provides a simple Flask-based API to predict Titanic passenger fare based on passenger details using a trained Linear Regression model. Folder Structure
titanic_api
  api/
    app.py
 model/
   model.pkl
train/
   train_model.py
requirements.txt
README.md
Setup Instructions
1.	Install requirements:    pip install -r requirements.txt
2.	Train the model:
   cd train    python train_model.py
3. Start the API:
   cd ../api
   python app.py
API Endpoint
POST /predict
Description:
Predict Titanic fare using passenger details.
Request Body (JSON):
{
  "pclass": 1,
  "age": 28,
  "sibsp": 0,
  "parch": 0
}
Response Body (JSON):
{
  "input": {
    "pclass": 1,
    "age": 28,
    "sibsp": 0,
    "parch": 0
  },
  "predicted_fare": 82.47
}
Testing
Using Python script (test_request.py): import requests
url = "http://127.0.0.1:5000/predict" data = {
  "pclass": 1,
  "age": 28,
  "sibsp": 0,
  "parch": 0
}
response = requests.post(url, json=data) print(response.json()) Or using PowerShell:
Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" `
-Method Post `
-Headers @{"Content-Type"="application/json"} `
-Body '{"pclass": 1, "age": 28, "sibsp": 0, "parch": 0}'
Dependencies
-	flask
-	pandas
-	seaborn
-	scikit-learn
Author
Muhammad Hammad - Titanic API project using Linear Regression and Flask.
