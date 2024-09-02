import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Установите ключ API OpenAI
openai.api_key = 'ВАШ_OPENAI_API_КЛЮЧ'  # Замените 'ВАШ_OPENAI_API_КЛЮЧ' на ваш реальный ключ

# Замените следующую ссылку на вашу фактическую ссылку на запись
BOOKING_LINK = "https://alacrity.simplybook.me/v2/"

@app.route('/ask', methods=)
def ask():
    data = request.json
    user_question = data.get("question")

    # Обработка вопроса с использованием GPT-4o Mini
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_question}
            ]
        )

        assistant_reply = response.choices.message  # Исправлено, чтобы правильно получить ответ

        # Ответ с добавленной ссылкой на запись
        answer_with_booking = f"{assistant_reply}\nЗаписаться можно по ссылке: {BOOKING_LINK}"

        return jsonify({"response": answer_with_booking}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
