
#import
from Text_to_Voice import speak_it
import datetime
import wikipedia

# Start welcome function
def start ():
    print("=> Hello, This is SPRITAN a chatbot AI")
    speak_it("Hello, This is SPRITAN a chatbot AI")
    print("=> Feel free to say hi or command to do something")
    speak_it("Feel free to say hi or command to do something")
    print("-------------------------------------------------------------------------------------")

#wish me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak_it("Good Morning!")

    elif hour>=12 and hour<18:
        speak_it("Good Afternoon!")   

    else:
        speak_it("Good Evening!")  

#wikipedia
 # Logic for executing tasks based on query
def wiki(query):
    speak_it('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak_it("According to Wikipedia")
    print(results)
    speak_it(results)
    
