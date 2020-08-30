# imports
from Text_to_Voice import speak_it
from Fx import start
from Fx import wishMe
from Fx import wiki

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

