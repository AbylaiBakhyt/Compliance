import requests
import json


api = "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"


def send_message(user_message, messages):
    # Добавляем сообщение пользователя в историю для отправки на API
    messages.append({"role": "user", "content": user_message})
    
    # Отправляем запрос к API
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api}",
        },
        data=json.dumps({
            # "model": "google/gemma-2-9b-it:free",
            # "model": "google/gemma-2-27b-it",
            "model": "openai/gpt-4o-mini-2024-07-18",
            "messages": messages
        })
    )

    # Получаем ответ от модели
    res = response.json()['choices'][0]['message']['content']
    # Добавляем ответ ассистента в историю
    messages.append({"role": "assistant", "content": res})
    return res