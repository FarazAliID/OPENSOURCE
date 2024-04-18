#!/usr/bin/python3 
#author: (MR X)

import os, sys, time, random, requests
import json, itertools, re
#from googlesearch import search
#mport duckduckgo_search as ddgo
from faker import Faker
from mailtm import Email
import wikipedia as wiki
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs

#> ------ [ Colours ] ------ <#
white = "\033[0m"
rad = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
blue = "\033[1;34m"
#> ------ [ Gen-Wordlist ] ------ <#
def createWordList():
	logo()
	chrs = input(" [+] Input Characters for Passlist : ")
	try:
		min_length = int(input(" [+] Input Minimum Password length : "))
	except ValueError:
		min_length = 4
	try:
		max_length = int(input(" [+] Input Maximum Password length : "))
	except ValueError:
		max_length = 6
	outputX = input(" [+] PassList Save as : ")
	output = open(outputX, 'w')
	print(" ------------------------------------------------------")
	print(f"    {green}{chrs}{white}")
	print(" ------------------------------------------------------")
	time.sleep(2)
	for n in range(min_length, max_length + 1):
		for xs in itertools.product(chrs, repeat=n):
			chars = ''.join(xs)
			output.write("%s\n" % chars)
			print(chars)
	lines_Pass = len((open(outputX,"r").read()).splitlines())
	output.close()
	print(" ------------------------------------------------------")
	print(f" [{green}+{white}] PassList Save As : {outputX}")
	print(f" [{green}+{white}] Total Passwords : {str(lines_Pass)}")
	print(f" [{green}+{white}] Length - Minimum / Maximum : {str(min_length)} / {str(max_length)}")
	print(" ------------------------------------------------------")
	input("")
	time.sleep(0.5)
	main()
#> ------ [ Install-Kalinethunter ] ------ <#
def kali_nethunter():
	logo()
	print(f"[{green}+{white}] Installing Kali Net Hunter Please - Wait")
	print(" ------------------------------------------------------")
	os.system("""termux-setup-storage
pkg install wget -y
wget -O install-nethunter-termux https://offs.ec/2MceZWr
chmod +x install-nethunter-termux
bash install-nethunter-termux""")
	input("")
	time.sleep(0.5)
	main()
#> ------ [ IP-Information ] ------ <#
def ip_info():
	logo()
	user_ip = input(" [+] Input Target IP Address : ")
	urlY = (f"http://ip-api.com/json/{user_ip}?lang=en")
	print(" ------------------------------------------------------")
	print(f"    target: {green}{user_ip}{white}")
	print(" ------------------------------------------------------")
	sess = requests.Session()
	data = sess.get(urlY).text
	data = json.loads(data)
	for key,values in data.items():
		print(f" [{green}+{white}] {str(key).capitalize()} : {str(values).capitalize()}")
	print(" ------------------------------------------------------")
	input("")
	time.sleep(1)
	main()
#> ------ [ Query Search ] ------ <#
def query_search():
	number = 1
	logo()
	query = input(f'[{green}+{white}] Input Keyword && Query : ').strip().split('--')
	print(" ------------------------------------------------------")
	for words in query: #\n
		results = search(words,num_results=20,sleep_interval=5,advanced=True)
		print(f"[{green}*{white}] Google Search Result [{words}]: ")
		for result in results:
			print(f" [{green}*{white}] Title {green}{number}{white} : {result.title} ")
			print(f" [{green}*{white}] URL : {result.url}")
			print(f" [{green}*{white}] Description : {result.description}\n")
			number +=1
		summary = wiki.summary(words)
		page = wiki.page(words)
		print(f'[{green}+{white}] Wikipedia : ')
		print(" ------------------------------------------------------")
		print(f'\t\t{summary}')
		print(f' [{green}*{white}] Title : {page.title}')
		print(f' [{green}*{white}] URL : {page.url}')
		print(f' [{green}*{white}] Description : {page.content}')
		duckgo_search = ddgo.DDGS()
		results = duckgo_search.text(words)
		print(" ------------------------------------------------------")
		print(f"[{green}*{white}] DuckDuckGo Search Result [{words}]: ")
		for result in results:
			title0 = (result['title']).split('-')[0]
			try:title1 = (result['title']).split('-')[1]
			except IndexError:title1 = 'None'
			url = result['href']
			content = result['body']
			print(f' [{green}*{white}] Title : {title1} [ {green}{title0}{white} ]')
			print(f' [{green}*{white}] URL : {url}')
			print(f' [{green}*{white}] Description : {content}')
#_________[ TempMailServer ]_________>>
def mailTm_listener(message):
	print(f"[{green}+{white}] Subject: " + message['subject'])
	print(f"[{green}+{white}] Content: " + message['text'] if message['text'] else message['html'])
def mailTM():
	logo()
	username = input(f"[{green}+{white}] Input Username [Random] : ")
	password = input(f"[{green}+{white}] Input Password [Random] : ")
	domain = input(f"[{green}+{white}] Input Domain [exelica.com] : ")
	mail = Email()
	if username in ['',' ']:username=None
	if password in ['',' ']:password=None
	if domain in ['',' ']:domain=None
	mail.register(username=username,password=password,domain=domain)
	print(f"\n[{green}+{white}] Email Adress: " + str(mail.address))
	print(f"[{green}+{white}] Waiting for new emails...")
	print(" ------------------------------------------------------")
	mail.start(mailTm_listener)
#> ------ [ Logo ] ------ <#
def logo():
    os.system('clear')
    print(f"""{white}   [{rad} Version 0.0.1 {white}]
___________.__    .__           .______________             
\__    ___/|  |__ |__|______  __| _/\_   _____/__.__. ____  
  |    |   |  |  \|  \_  __ \/ __ |  |    __ <   |  |/ __ \ 
  |    |   |   Y  \  ||  | \/ /_/ |  |        \___  \  ___/ 
  |____|   |___|  /__||__|  \____ | /_______  / ____|\___  >
                \/               \/         \/\/         \/ """)
    print(f" #> ---------------< [ {green}Third Eye{white} ] >---------------- <# ")
    print(f"{green} No Technology thats connected to internet is Unhackable{white}")
    print(" ------------------------------------------------------")
#> ------ [ Main ] ------ <#
def main():
    logo()
    print("")
    print(f" #> ---------------< [ {green}Main Menu{white} ] >---------------- <# ")
    print(f" [{green}01{white}] Wordlist generator ")
    print(f" [{green}02{white}] Install Kali NetHunter (rootless)")
    print(f" [{green}03{white}] IP Address Information")
    print(f" [{green}04{white}] Search Query [google,wikipedia,duckduckgo]")
    print(f" [{green}05{white}] TempMail Server [domain:]")
    print(f" [{green}06{white}] ")
    print(f" [{green}07{white}] ")
    print(f" [{green}08{white}] ")
    print(f" [{green}09{white}] ")
    print(f" [{green}10{white}] ")
    print(f" [{green}11{white}] ")
    print(f" [{green}12{white}] ")
    print(f" [{green}13{white}] ")
    print(f" [{green}14{white}] ")
    print(f" [{green}15{white}] ")
    mninp = input(f"[{green}->{white}] Input an option : ")
    if mninp in ['01','1']:
        createWordList()
    elif mninp in ['02','2']:
        kali_nethunter()
    elif mninp in ['03','3']:
        ip_info()
    elif mninp in ['04','4']:
        query_search()
    elif mninp in ['05','5']:
        mailTM()
if __name__=="__main__":
	main()
