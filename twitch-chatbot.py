from lib import twitch_chat_irc
from datetime import datetime

# Constants
TWITCH_CHANNEL_NAME = 'stellaric'

connection = None

def twitch_connect():
    print("Connecting & Logging in to Twitch")
    connection = twitch_chat_irc.TwitchChatIRC()

twitch_connect()

def twitch_send_message(message):
    connection.send(TWITCH_CHANNEL_NAME, message)

def twitch_on_receive_message(message_data):
	print(f"{datetime.now()} - {message_data['display-name']}: {message_data['message']}")

print(f"\nListening for messages in channel `{TWITCH_CHANNEL_NAME}`\n")
connection.listen(TWITCH_CHANNEL_NAME, on_message=twitch_on_receive_message)

connection.close()