import CreateAccount
from colorama import Fore, Back, Style
from signup import *
def main():
    print(Back.YELLOW+"                                                                                                            "+Style.RESET_ALL)


    print(Fore.CYAN+" "+Style.BRIGHT+"                                   Email Application System                                                              ")

    print(Back.YELLOW+"                                                                                                            "+Style.RESET_ALL)
    print("  ")
    try:
     print("\t 1]Sign Up")
     print("\t 2]Create Account")
     choice=input("\tEnter Your  Choice (1 or 2):")
     if(choice == "1"):
       sign()
     elif(choice == "2"):
        CreateAccount.createaccount()
     else:
        print(Fore.RED+"Please select correct choice"+Style.RESET_ALL)
    except Exception as e:
        print(e)

main()