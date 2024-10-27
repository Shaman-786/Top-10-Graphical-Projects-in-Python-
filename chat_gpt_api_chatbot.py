import requests

def get_response(self, message):
    headers = {
        'Authorization': f'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'text-davinci-003',  # This can vary based on the model you're using
        'prompt': message,
        'max_tokens': 150,
    }
    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['text'].strip() if 'choices' in response_json and response_json['choices'] else "Sorry, I couldn't respond."
