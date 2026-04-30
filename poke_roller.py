import requests
import time
import random
import os

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('AUTH_TOKEN')
CHANNEL_ID = '1180951373664227469'

headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json'
}


def send_message(message: str):
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'
    data = {
        'content': message
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print(f'Message sent successfully at {time.ctime()}')
        else:
            print(f'Failed to send message: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'An error occurred: {e}')


last_hour_sent = -1
print("Starting message sender...")
message = "$p"

# Send message at every 2h interval (2am, 4am, 6am, etc.), at random minute and second
while True:
    current_time = time.localtime()
    if current_time.tm_hour % 2 == 0 and last_hour_sent != current_time.tm_hour:
        time.sleep(60 * random.randint(1, 60)) # Wait between 1 and 60 minutes
        send_message(message)
        last_hour_sent = current_time.tm_hour
    else:
        time.sleep(1800)  # Check every 30 minutes