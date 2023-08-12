
whisper https://github.com/openai/whisper
real time transcription with whisper https://github.com/davabase/whisper_real_time/blob/master/transcribe_demo.py

# flow
- pull twitch video (or audio) feed
- separate audio feed / ingest over time
- split audio feed into sections for speech to text to use
- speech to text audio file into words that streamer said
- take streamer said, into chatgpt "How would you respond to live streamer who says this: message"
- postprocessing of what chatgpt is sending to make less formal
  - random misspellings / capitalization
  - capitalize first letter only
  - swap their's
  - full-lowercase only
- [x] twitch chat bot -> send response messages

# stretch goals
- make an argumentative version