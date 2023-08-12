# from https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/

import socket
from emoji import demojize
from datetime import datetime
import re
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

connection_data = ('irc.chat.twitch.tv', 6667)
token = 'oauth:6ab56xhkvzb1nlxzajjyxmjqe9zhxw'
user = 'replyguyai'
channel = '#stellaric'
readbuffer = ''

server = socket.socket()
server.connect(connection_data)
server.send(bytes(f'PASS {token}\r\n', 'utf-8'))
server.send(bytes(f'NICK {user}\r\n', 'utf-8'))
server.send(bytes(f'JOIN {channel}\r\n', 'utf-8'))

print(server)
while True:
    resp = server.recv(2048).decode('utf-8') # you can also play around with the 2048 value in there and see what kind of jargon you get back!

    if resp.startswith('PING'):
        server.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:
        msg = demojize(resp)
        logging.info(msg)
        print(f"raw socket message: {msg}")

        # time_logged = msg.split()[0].strip()
        # time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

        try:
            # username_message = msg.split('—')[1:]
            # username_message = '—'.join(username_message).strip()

            username, channel, message = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', msg).groups()
            print(f"({channel}) {username}: {message}") #TimeLogged: {time_logged}
            
            send_message = f"PRIVMSG #{channel} :Hello {username}{message}\r\n"
            print(f"send_message {send_message}")
            server.send(bytes(send_message, 'utf-8'))
        except Exception as e:
            print(f"Exception {e}")
            pass
