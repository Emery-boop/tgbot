from telethon import TelegramClient, events
import requests

# Step 1: Your Telegram API credentials
api_id = 12345678  # Replace with your API ID
api_hash = 'your_api_hash_here'  # Replace with your API hash

# Optional: Telegram bot token if you're using a bot to send
bot_token = 'your_bot_token_here'

# Step 2: Source & destination
source_channel = '@solwhaletrending'  # No @ symbol
destination_channel = '@gustavogrinch'  # Can use @ if public

# Step 3: Initialize Telegram user client
client = TelegramClient('forwarder_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    msg = event.message.message
    # Forwarding message using bot API
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": destination_channel,
        "text": msg
    }
    response = requests.post(send_url, data=payload)
    print(f"Copied: {msg[:40]}...")

print("🚀 Forwarding from public to public...")
client.start()
client.run_until_disconnected()
