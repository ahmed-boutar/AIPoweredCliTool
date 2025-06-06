import boto3
import json
from config import Config

bedrock = boto3.client("bedrock-runtime", region_name=Config.AWS_REGION)

def summarize_text(text: str) -> str:
    try:
        input_data = {
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": f"Summarize the following text while preserving the main points and key details:\n{text}"
                            }
                        ]  
                    }
                ],
                "inferenceConfig": {
                    "max_new_tokens": 2000,
                    "temperature": 0.7,
                    "topP": 0.9
                }
            }

        response = bedrock.invoke_model(
                modelId=Config.BEDROCK_MODEL_ID,
                body=json.dumps(input_data),
                accept='application/json',
                contentType='application/json'
            )

        response_body = response['body'].read().decode('utf-8')
        response_data = json.loads(response_body)
        
        # Extract the response text
        content_list = response_data.get('output', {}).get('message', {}).get('content', [])
        formatted_response = "\n".join([item.get('text', '') for item in content_list])

        return formatted_response
    except Exception as e:
        return f"Error: {str(e)}"
    
def main():
    text_to_summarize = "My name is John Doe. I am a software engineer with over 10 years of experience in developing scalable applications. I have worked with various technologies including Python, Java, and AWS. In my free time, I enjoy hiking and photography."
    summary = summarize_text(text_to_summarize)
    print("Summary:", summary)

if __name__ == "__main__":
    main()