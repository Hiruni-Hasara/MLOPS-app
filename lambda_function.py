import json
import joblib
import boto3
import os

# Load model from local (after copy from S3 in Dockerfile)
model = joblib.load("model.pkl")

def lambda_handler(event, context):
    try:
        input_data = json.loads(event["body"])
        features = input_data["features"]
        prediction = model.predict([features])[0]
        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": int(prediction)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
