import speech_recognition as sr
import sys

#read duration from the arguments
duration = int("2")

# initialize the recognizer
r = sr.Recognizer()
print("Please talk")

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    # Language
    # text = r.recognize_google(audio_data, language="es-ES")
    
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)