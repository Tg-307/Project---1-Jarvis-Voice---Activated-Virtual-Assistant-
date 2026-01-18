from gtts import gTTS
from playsound import playsound
import os
import time
# import pyttsx3

# def speak(text):
#     print("Jarvis: " + text)
#     pyttsx3.speak(text)


def speak(text):
    """
    Generates speech using gTTS, saves it, and plays it.
    This version includes a loop to keep the script alive.
    """
    try:
        tts = gTTS(text=text, lang='en')
        audio_file = "speech.mp3"
        tts.save(audio_file)
        
        # print("Jarvis: " + text)
        
        # This will now work as intended
        playsound(audio_file) 
        
        # Clean up the audio file after playing
        os.remove(audio_file)

    except Exception as e:
        print(f"An error occurred: {e}")
