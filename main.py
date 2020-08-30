# imports
from Text_to_Voice import speak_it
from Fx import start

# Global Variables
requestAI=""
requestAIs=""
i=0

# working
start()
while requestAIs!="exit":
    flag = 0
    requestAI=input("You     => ")
    requestAIs=requestAI.lower() #can be changed latter
    