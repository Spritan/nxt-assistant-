
# imports
import speech_recognition as sr
import pyttsx3

# Audio
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice', voices[0].id)

# Function
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
a=takeCommand()
print(a)