# imports
import mysql.connector

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

#fuctions to input
def add_respond(u_input,p_output):
    a1 = (u_input, p_output)
    mycursor.execute(sqlformula,a1)
    mydb.commit()
# add_respond("is this heaven?","Plz refer to God")
