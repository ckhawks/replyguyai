from lib import twitch_chat_irc
from datetime import datetime

# Constants
TWITCH_CHANNEL_NAME = 'stellaric'
SELF_NAME = 'replyguyai'
DEBUG_DO_NOT_SEND_MESSAGES = True

connection = None

def twitch_connect():
    print("Connecting & Logging in to Twitch")
    connection = twitch_chat_irc.TwitchChatIRC()

twitch_connect()
print(f'{connection}')

def twitch_send_message(message):
    print(f"[ME] {SELF_NAME}: {message}")
    if not DEBUG_DO_NOT_SEND_MESSAGES:
        connection.send(TWITCH_CHANNEL_NAME, message)

def twitch_on_receive_message(message_data):
	print(f"{datetime.now()} - {message_data['display-name']}: {message_data['message']}")

print(f"\nListening for messages in channel `{TWITCH_CHANNEL_NAME}`\n")
connection.listen(TWITCH_CHANNEL_NAME, on_message=twitch_on_receive_message)

connection.close()