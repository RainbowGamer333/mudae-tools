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

send_message('$p')