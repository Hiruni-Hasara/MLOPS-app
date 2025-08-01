import json
import pickle
import boto3

s3 = boto3.client("s3")
model = None

def load_model():
    global model
    if model is None:
        response = s3.get_object(Bucket="mlops-app-bucket", Key="model.pkl")
        model = pickle.loads(response['Body'].read())

def lambda_handler(event, context):
    load_model()
    body = json.loads(event["body"])
    input_data = [body["features"]]  # Expecting a list of values
    prediction = model.predict(input_data)
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": int(prediction[0])})
    }
