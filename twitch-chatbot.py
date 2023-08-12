from lib import twitch_chat_irc

TWITCH_CHANNEL_NAME = 'stellaric'
print(twitch_chat_irc)

print("Connecting to Twitch")
connection = twitch_chat_irc.TwitchChatIRC()

print("Sending message")
message = 'Hello world!'
connection.send(TWITCH_CHANNEL_NAME, message)

def do_something(message):
	print(f"Received: {message}")

connection.listen(TWITCH_CHANNEL_NAME, on_message=do_something)

