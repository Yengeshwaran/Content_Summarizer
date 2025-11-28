import boto3

def get_summary(input_text, uploaded_file):
    
    # Read bytes from the user-uploaded PDF
    doc_bytes = uploaded_file.read()

    doc_message = {
        "role": "user",
        "content": [
            {
                "document": {
                    "name": "Document 1",
                    "format": "pdf",
                    "source": {
                        "bytes": doc_bytes  # using uploaded file bytes
                    }
                }
            },
            { "text": input_text }
        ]
    }
    
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[doc_message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
    )
    
    return response['output']['message']['content'][0]['text']
