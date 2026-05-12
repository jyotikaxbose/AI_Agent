import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    if len(message) > 4000:
        message = message[:4000] + "\n\n... [truncated]"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Message sent to Telegram!")
        return True
    else:
        print(f"Telegram error: {response.text}")
        return False

if __name__ == "__main__":
    send_telegram_message("Test message from AI News Agent!")