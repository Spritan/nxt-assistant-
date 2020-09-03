# imports
import mysql.connector
from Text_to_Voice import speak_it

# configuration
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="BhSaPnPh02)#23",
    database = "aidb"
)

# logic
mycursor=mydb.cursor()

sqlformula="INSERT INTO respond (ques,ans) VALUES (%s, %s)"
sqlformula2 = "SELECT ans FROM respond WHERE ques = "

#fuctions to input
def add_respond(u_input,p_output):
    a1 = (u_input, p_output)
    mycursor.execute(sqlformula,a1)
    mydb.commit()

#function to output
def get_respond(u_input):
    a2 = sqlformula2+"'"+u_input+"'"
    mycursor.execute(a2)
    myresult=mycursor.fetchone()
    return myresult


p_output = get_respond("are you happy?")
speak_it(p_output)
print(p_output)



