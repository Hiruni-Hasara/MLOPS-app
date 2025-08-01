FROM public.ecr.aws/lambda/python:3.9

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add Lambda function code
COPY lambda_function.py .

# Define Lambda handler
CMD ["lambda_function.lambda_handler"]
