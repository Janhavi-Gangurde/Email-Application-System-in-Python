import datetime
from colorama import Fore, Back, Style
from datetime import date
import mysql.connector
db=mysql.connector.Connect(
    host="localhost",
    user="root",
    password="",
    database="computer"
)
if db.is_connected():
   mycursor = db.cursor()
def emailpage():
   print(Fore.BLUE+"==========================================================")
   print("**************Gmail***************************************")
   print("=========================================================="+Style.RESET_ALL)
   print(Fore.CYAN+"\t\t1]All Mail")
   print("\t\t2]Important")
   print("\t\t3]Sent")
   print("\t\t4]Spam")
   print("\t\t5]Social")
   print("\t\t6]Compose")
   print("\t\t7]Log Out"+Style.RESET_ALL)
   choice=int(input("Select any Choice:"))
   if(choice==1):
      f=open("file1.txt",'r')
      z=f.read()
      print(z)
      emailpage()
   elif(choice==2):
      f = open("file2.txt", 'r')
      z = f.read()
      print(z)
      emailpage()
   elif(choice==3):
      f = open("file3.txt", 'r')
      z = f.read()
      print(z)
      emailpage()
   elif(choice==4):
      f = open("file4.txt", 'r')
      z = f.read()
      print(z)
      emailpage()
   elif(choice==5):
      f = open("file1.txt", 'r')
      z = f.read()
      print(z)
      emailpage()
   elif(choice==6):
      insertQuery = ("SELECT user from username")
      mycursor.execute(insertQuery)
      username = mycursor.fetchall()
      db.commit()
      From=username[0][0]
      print(" ")
      print("\tFrom:",From)
      To=input("\tTo:")
      emailcheck(To)
      message=input("\tmessage:")
      print(" ")
      send=input("Send or Not:")
      if(send=="send"):
         print("Send Successfully")
         time = datetime.datetime.now()
         Time = str(time.time())
         today = date.today()
         d1 = today.strftime("%d/%m/%Y")
         f = open("file3.txt", "w")
         f.write("From:" + From + "")
         f.write("\nTo:" + To + "")
         f.write("\nMessage:" + message + "")
         f.write("\nDate:" + d1 + "")
         f.write("\nTime:" + Time + "")
         f.close()
         emailpage()
      elif(send=="not"):
         emailpage()

      else:
         print(Fore.RED+"Please select correct choice"+Style.RESET_ALL)
   elif(choice==7):
    logout=input("You want log out : Yes/No:")
    logout=logout.lower()
    if(logout=="yes"):
       sql = "DELETE from username"
       mycursor.execute(sql)
       db.commit()
       print(Fore.LIGHTMAGENTA_EX+"Logout sucessfully"+Style.RESET_ALL)
       exit()
    elif(logout=="no"):
       emailpage()
   else:
      print(Fore.RED+"Please select correct choice:"+Style.RESET_ALL)
      emailpage()

   db.close()
def emailcheck(id):
   import re
   regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
   username=id
   if (re.search(regex, username)):
      pass
   else:
      validemailid = input(Fore.RED+"Please Enter valid Email ID (xyz@gmail.com):"+Style.RESET_ALL)
      if (re.search(regex, validemailid)):
         pass
      else:
         print("Enter Valid Email Id next time")
         emailpage()



