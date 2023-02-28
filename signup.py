from Emailpage import *
from colorama import Fore, Back, Style
import mysql.connector
db=mysql.connector.Connect(
    host="localhost",
    user="root",
    password="",
    database="computer"
)
if db.is_connected():
    mycursor = db.cursor()
def sign():
 choice=input(Fore.YELLOW+"Enter you want to:1]Signup 2]LogOut :"+Style.RESET_ALL)
 choice=choice.lower()
 if(choice=="signup"):
   username=input("\tEnter Username:")
   password=input("\tEnter Password:")
   insertQuery = ("SELECT username,password from userdetails where username=%s AND password=%s")
   mycursor.execute(insertQuery, (str(username),str(password)))
   result = mycursor.fetchall()

   if(len(result)!=0):
    sql = "INSERT INTO  username (user) VALUES (%s)"
    val = (username,)
    mycursor.execute(sql, val)
    db.commit()
    emailpage()

   else:
    print(Fore.RED+"Wrong username and Password"+Style.RESET_ALL)
    username = input("\tEnter Username:")
    password = input("\tEnter Password:")
    insertQuery = ("SELECT username,password from userdetails where username=%s AND password=%s")
    mycursor.execute(insertQuery, (str(username), str(password)))
    result = mycursor.fetchall()
    if (len(result) != 0):
     sql = "INSERT INTO  username (user) VALUES (%s)"
     val = (username,)
     mycursor.execute(sql, val)
     db.commit()
     emailpage()

    else:
     print(Fore.RED+"Enter correct Username and Password"+Style.RESET_ALL)
     sql = "DELETE from username"
     mycursor.execute(sql)
     db.commit()
     exit()

 elif(choice=="logout"):
  sql = "DELETE from username"
  mycursor.execute(sql)
  db.commit()
  exit()

 else:
  print(Fore.RED+"Please Enter correct choice"+Style.RESET_ALL)
  sql = "DELETE from username"
  mycursor.execute(sql)
  db.commit()
 db.close()
