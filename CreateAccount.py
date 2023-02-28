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
def createaccount():
    print(Fore.LIGHTMAGENTA_EX+"*********************Enter Your Correct Details**********************************"+Style.RESET_ALL)
    global username
    name=input("\tEnter Your Name:")
    surname=input("\tEnter Your Surname:")
    date=input("\tEnter date of Birth dd/mm/yy:")
    gender=input("\tEnter Gender 1]Male 2]Female:")
    username=input("\tEnter Username:")
    username=username.lower()
    checkusername(username)
    if(len(result)!=0):
        print(Fore.RED+"Username is existed"+Style.RESET_ALL)
        username=input("\tEnter Username:")
        username=username.lower()
        checkusername(username)
        if (len(result)!=0):
         print(Fore.RED+"Username all ready is existed"+Style.RESET_ALL)
         print(Fore.RED+"Please Enter valid Username another time"+Style.RESET_ALL)
         exit()
        else:
         emailid(username)
    else:
     emailid(username)

    password=input("\tEnter Passowrd:")
    if(password_validate(password)):
        correctPassword(name, surname, date, gender, password)
    else:
     password=input("\tEnter Password valid Password:")
     if(password_validate(password)):
         correctPassword(name, surname, date, gender, password)
     else:
        print(Fore.RED+"Please Enter valid Password next time"+Style.RESET_ALL)
        exit()


def password_validate(password):
     SpecialSymbol = ['$', '@', '#', '%']
     val = True

     if len(password) < 6:
            print(Fore.RED+'length should be at least 6')
            val = False

     if len(password) > 20:
            print(Fore.RED+'length should be not be greater than 8')
            val = False

     if not any(char.isdigit() for char in password):
            print(Fore.RED+'Password should have at least one numeral')
            val = False

     if not any(char.isupper() for char in password):
            print(Fore.RED+'Password should have at least one uppercase letter')
            val = False

     if not any(char.islower() for char in password):
            print(Fore.RED+'Password should have at least one lowercase letter')
            val = False

     if not any(char in SpecialSymbol for char in password):
            print(Fore.RED+'Password should have at least one of the symbols $@#'+Style.RESET_ALL)
            val = False
     if val:
      return val
def correctPassword(name,surname,date,gender,password):
    print(Fore.LIGHTBLUE_EX+"----------------------------------------------------------------------------------------------------------")
    print("********************************************Check Your Information******************************************")
    print("-----------------------------------------------------------------------------------------------------------"+Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX+"Name:"+Style.RESET_ALL, name, surname)
    print(Fore.LIGHTGREEN_EX+"Date Of Birth:"+Style.RESET_ALL, date)
    print(Fore.LIGHTGREEN_EX+"Gender:"+Style.RESET_ALL, gender)
    print(Fore.LIGHTGREEN_EX+"Username:"+Style.RESET_ALL,username)
    fullname=name+surname
    confirm = input("Enter Confirm Password:")
    if (password == confirm):
        print(Fore.LIGHTMAGENTA_EX+"Your Account Create Successfully"+Style.RESET_ALL)
        sql = "INSERT INTO  userdetails (name,birthdate,username,password) VALUES (%s, %s,%s,%s)"
        val = (fullname,date,username,password)
        mycursor.execute(sql, val)
        db.commit()
        choice = input("\tEnter choice 1]Signup 2]Logout:")
        choice=choice.lower()
        if (choice =="signup"):
            emailpage()
        elif (choice =="logout"):
            exit()
        else:
            print(Fore.RED+"Please enter correct choice:"+Style.RESET_ALL)
    else:
        correct = input(Fore.RED+"Please Enter Correct Password:"+Style.RESET_ALL)
        if (password == correct):
            print(Fore.LIGHTMAGENTA_EX+"Your Account Create Successfully"+Style.RESET_ALL)
            sql = "INSERT INTO  userdetails (name,birthdate,username,password) VALUES (%s, %s,%s,%s)"
            val = (fullname, date, username, password)
            mycursor.execute(sql, val)
            db.commit()
            choice = input("\tEnter choice 1]Signup 2]Logout:")
            choice=choice.lower()
            if (choice =="signup"):
                emailpage()
            elif (choice =="logout"):
                exit()
            else:
                print(Fore.RED+"Please enter correct choice:"+Style.RESET_ALL)

        else:
            print(Fore.RED+"your Enter valid password  next time"+Style.RESET_ALL)

    db.close()



def emailid(username):
    import re
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, username)):
        pass
    else:
     print(Fore.RED+"Please Enter Valid Email Id next time"+Style.RESET_ALL)
     exit()
def checkusername(user):
    global result
    insertQuery=("SELECT username from userdetails where username=%s")
    mycursor.execute(insertQuery,(str(user),))
    result = mycursor.fetchall()




