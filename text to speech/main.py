
from gtts import gTTS
import os

# Open the file containing text to be converted to speech
with open('sample.txt', 'r') as file:
    text = file.read()

# Create an instance of gTTS
tts = gTTS(text)

# Save the speech as an MP3 file
tts.save("audio.mp3")

# Play the speech using the default media player on your computer
os.system("audio.mp3")
