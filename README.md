# nxt-assistant
 
This is a Chatbot written in **Python 3.64** with a **MariaDb** database backend.  
The logic is very simple - the ChatBot stores bag-of-word associations for responses to a previous sentence and uses this to try to match future responses. 
This is not aimed at any real practical task, it is just a framework for experimenting with and developing further.

## Python Library Dependencies ##

1. webbrower https://docs.python.org/3.6/library/webbrowser.html (python -m webbrowser -t "http://www.python.org")
2. smtplib https://docs.python.org/3.6/library/smtplib.html (pip install smtplib)
3. wikipedia https://pypi.org/project/wikipedia/
4. requests https://pypi.org/project/requests/
5. pickle https://docs.python.org/3/library/pickle.html (pip install pickle-mixin)
6. pyttsx3 https://pypi.org/project/pyttsx3/
7. pyaudio https://pypi.org/project/PyAudio/
8. speech_recognition https://pypi.org/project/SpeechRecognition/
9. mysql.connector https://pypi.org/project/mysql-connector-python/

## All Files ##

1.  Main.py           : The main code where all execution occurs
2.  User.py           : user profile creation. (under work)
3.  Text_to_voice.py  : The funtion and configuration for text to voice functionality.
4.  Sql_connection.py : The functiona and configuration of the implementation of Maria.db
5.  Speech_to_text.py : The functiona and configuration of the implementation of voice recognition
6.  weather.py        : Geting current weather report via openweathermap API
7.  loginscreen.py    : Multiuser selection and password protection implementaion. (under work)
8.  Fx.py             : This module is for all random feature and functions which are not too big to have separate modules.
9.  Encrytion.py      : The function for hashing password and encryption/decryption of config files (under work)
10. credentials.py    : The functiona and configuration of the implementation of user login management (not yet implemented)

