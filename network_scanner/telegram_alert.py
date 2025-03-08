from telegram import Bot

# Telegram Bot Config
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
TELEGRAM_CHAT_ID = "your-chat-id"

def send_telegram_alert(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("[✅] Telegram alert sent successfully!")
    except Exception as e:
        print(f"[❌] Error sending Telegram alert: {e}")

# Example Usage
if __name__ == "__main__":
    send_telegram_alert("🚨 Security Alert: Unauthorized device detected!")
