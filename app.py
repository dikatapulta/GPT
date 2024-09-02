from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Замените 'YOUR_API_KEY' на ваш ключ API OpenAI
openai.api_key = 'YOUR_API_KEY'

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('input')
    
    # Обращение к API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    
    answer = response['choices'][0]['message']['content']
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(port=5000)
