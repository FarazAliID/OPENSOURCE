#!/bin/python3
"""
Faraz Ali ID

"""
#_________[ IMPORTING MODULES ]_________>>
from os import system as cmd 
from time import sleep as slp 
from random import randint as rint 
from random import choice as rsrt
#_________[ BASIC COLOURS ]_________>>
red = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
blue = "\033[1;35m"
#_________[ LIST / LOOP ]_________>>
numX = []
mailX = []
unamX = []
uidX = []
#_________[ LOGO ]_________>>
def logo():
    cmd("clear")
    print(f"""{white} {white}""")
    print(f"{white}------------------------------------------------")
    print(f"    [{green}+{white}] Tool Name : Zero ( {blue}FB Multi Brute Force{white} )")
    print(f"    [{green}+{white}] Version : 0.0.1")
    print(f"    [{green}+{white}] Creater : ")
    print(f"{white}------------------------------------------------")
#_________[ RANDOM NUMBER ]_________>>
def random_number():
    logo()
    print(" Input Any Phone Number With Country Code ")
    print(f" EX {green}(PAK){white}: 923445440123 ")
    print(f" EX {green}(IND){white}: 913445440123 ")
    print(f"{white}------------------------------------------------")
    number = input(f"[{green}+{white}] Input Number Without(+) : ")
    try:
        number = int(number)
    except ValueError:
        print(f"{red} Wrong Input Try Again {white}")
        slp(2)
        main()
    try:
        limit = int(input("[+] Input limit dump : "))
    except ValueError:
        limit = 5000
    codeX_length = len(str(number))
    for i in range(limit):
        codeX = str(number)[((int(codeX_length))-7):]
        numX.append(str(number)+"|"+str(codeX))
#_________[ RANDOM EMAIL ]_________>>
def random_email():
    logo()
    print(" Input Any Name For Email Dump ")
    print(f" EX {green}(1){white}: Bilal Haider ID ")
    print(f" EX {green}(2){white}: Faraz Ali ID ")
    print(f"{white}------------------------------------------------")
    name = input(f"[{green}+{white}] Input Random Name : ")
    username = (name.replace(" ","")).lower()
    try:
        limit = int(input(f"[{green}+{white}] Input limit dump : "))
    except ValueError:
        limit = 5000
    domain = input(f"[{green}+{white}] Input Mail Domain : ")
    for i in range(limit):
        mail = username+str(i)+domain
        mailX.append(mail+"|"+name)
#___________[ RANDOM USERNAME ]________>>
def random_username():
    logo()
    print(" Input Any Name For UserName Dump ")
    print(f" EX {green}(1){white}: Bilal Haider ID ")
    print(f" EX {green}(2){white}: Faraz Ali ID ")
    print(f"{white}------------------------------------------------")
    name = input(f"[{green}+{white}] Input Random Name : ")
    username = (name.replace(" ",".")).lower()
    try:
        limit = int(input(f"[{green}+{white}] Input limit dump : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        unamX.append((username+"."+str(i))+"|"+name)
    print(unamX)
#___________[ RANDOM UID ]________>>
def random_UID():
    logo()
    print(" Input Any UID For User ID Dump ")
    print(f" EX {green}(1){white}: 100091*******")
    print(f" EX {green}(2){white}: 100000*******")
    print(f"{white}------------------------------------------------")
    uid = input(f"[{green}+{white}] Input Random UID : ")
    try:
        uid = int(uid)
    except ValueError:
        uid = rint(100000000000000,1000900000000000)
    try:
        limit = int(input(f"[{green}+{white}] Input limit dump : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        uid = uid+(i+1)
        pwduid = rsrt(["786786",
                       "123456",
                       "123456789",
                       "102030",
                       "112233"])
        uidX.append(str(uid)+"|"+pwduid)
    print(uidX)
#_________[ MAIN MENU ]_________>>
def main():
    logo()
    print(f"[{green}01{white}] Random Number Cracking")
    print(f"[{green}02{white}] Random Email Cracking")
    print(f"[{green}03{white}] Random UserName Cracking")
    print(f"[{green}04{white}] Random Random UID Cracking")
    print(f"[{green}00{white}] Exit ")
    print(f"{white}------------------------------------------------")
    mch = input(f"[{green}>>{white}] Choose an option : ")
    if mch in ["1","01"]:random_number()
    elif mch in ["2","02"]:random_email()
    elif mch in ["3","03"]:random_username()
    elif mch in ["4","04"]:random_UID()
    elif mch in {"0","00"}:exit()
    else:
        slp(1)
        main()
if __name__=="__main__":
    main()