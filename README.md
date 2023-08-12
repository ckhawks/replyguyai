Twitch chat bot that listens to the streamer and queries ChatGPT for a response

# flow
- [ ] pull twitch video (or audio) feed
- [ ] separate audio feed / ingest over time
- [ ] split audio feed into sections for speech to text to use
- [x] speech to text audio file into words that streamer said
- [ ] take streamer said, into chatgpt "How would you respond to live streamer who says this: message"
- [ ] postprocessing of what chatgpt is sending to make less formal
  - random misspellings / capitalization
  - capitalize first letter only
  - swap their's
  - full-lowercase only
- [x] twitch chat bot -> send response messages
  - [x] do with irc

# stretch goals
- [ ] make an argumentative version

# remember
fast_bread=true !!!!

# references
- whisper https://github.com/openai/whisper  
- real time transcription with whisper https://github.com/davabase/whisper_real_time/blob/master/transcribe_demo.py
- twitch websocket stuff
    - https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/
    - https://medium.com/@a_matare/how-to-make-a-twitch-bot-in-python-that-listens-twytch-v2-10560fed0c70
    - https://github.com/scmanjarrez/twitch-chat-irc