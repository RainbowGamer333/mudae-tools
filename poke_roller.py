import requests
import time
import random
import os

from dotenv import load_dotenv
load_dotenv()

token_list = ['ROMAIN_AUTH_TOKEN', 'LOGANN_AUTH_TOKEN']
TOKENS = [os.getenv(token) for token in token_list if os.getenv(token) != -1]

CHANNEL_ID = '1180951373664227469'
URL = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

if not TOKENS:
    print("Error: No valid authentication tokens found in environment variables.")
    exit(1)

def send_message(message: str, headers: dict):
    data = {
        'content': message
    }

    try:
        response = requests.post(URL, json=data, headers=headers)
        if response.status_code == 200:
            print(f'Message sent successfully at {time.ctime()}')
        else:
            print(f'Failed to send message: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    for token in TOKENS:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        send_message('$p', headers)