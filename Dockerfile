FROM public.ecr.aws/lambda/python:3.9

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY lambda_function.py .
COPY model.pkl .

CMD ["lambda_function.lambda_handler"]
