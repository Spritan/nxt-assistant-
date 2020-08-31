# imports
from Text_to_Voice import speak_it
from Fx import start
from Fx import wishMe
from Fx import wiki
from Fx import sendEmail
from Fx import web_s
import datetime

# Global Variables
requestAI=""
requestAIs=""
i=0

# working
wishMe()
start()
while requestAIs!="exit":
    flag = 0
    requestAI=input("You     => ")
    requestAIs=requestAI.lower() #can be changed latter
    if 'wikipedia' in requestAIs:
        wiki(requestAIs)
    elif 'send email' in requestAIs:
        try:
            to = input("To: ")
            speak_it("What should I say?")
            content = input()
            sendEmail(to, content)
            speak_it("Email has been sent!")
        except Exception as e:
            print(e)
            speak_it("Sorry my friend. I am not able to send this email")
    elif 'current time' in requestAIs:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak_it("Sir, the time is"+strTime)
        print("SPRITAN => Sir, the time is "+strTime)
    elif 'webopen' in requestAIs:
        web_s(requestAIs)
        print("dw")
