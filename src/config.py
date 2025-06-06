import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    AWS_REGION = os.environ.get('AWS_REGION') or 'us-east-1'
    BEDROCK_MODEL_ID = os.environ.get('BEDROCK_MODEL_ID') or 'amazon.nova-micro-v1:0'