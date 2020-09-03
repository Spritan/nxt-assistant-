#intro
"""
    this is as name suggest text to voice module so as to make the program speak
"""
# import
import pyttsx3


# initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function
def speak_it(audio):
    engine.say(audio)
    engine.runAndWait()
