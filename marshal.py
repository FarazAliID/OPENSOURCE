#Coded By : Faraz Ali ID
#Python3 Marshal Encoded 
import os
import sys
import time
import marshal
os.system("clear")
logo = ("""\x1b[1;97m______       _____       ___  ___               _           _ 
| ___ \     |____ |      |  \/  |              | |         | |
| |_/ /   _     / /______| .  . | __ _ _ __ ___| |__   __ _| |
|  __/ | | |    \ \______| |\/| |/ _` | '__/ __| '_ \ / _` | |
| |  | |_| |.___/ /      | |  | | (_| | |  \__ \ | | | (_| | |
\_|   \__, |\____/       \_|  |_/\__,_|_|  |___/_| |_|\__,_|_|
       __/ |                                                  
      |___/                           \x1b[1;91m Version : 0.0.1 \x1b[1;97m""")
print(logo)
x = input("\n[*] Enter Source File : ")
try:
	q = x.split('.')
	u = q[0] + "_enc.py"
except:
	u = input("[*] Encoded File Save As : ")
f = int(input("\n[*] Enter Encoding layer Limit : "))
print("")
a = open(x).read()
try:
	j = 0
	for i in range(f):
		j += 1
		m = compile(a, ' ', 'exec')
		k = marshal.dumps(m)
		t = '#Encoded By : FARAZ ALI ID \n#Encryption : Py3 Marshal\n#Py3 Version : 3.10.4\n\nimport marshal\nexec(marshal.loads('+repr(k)+'))'
		time.sleep(0.004)
		print("\x1b[1;97m[✓] Encoding layer >> " + str(j))
except ValueError:
	exit("\n[>>] Wrong Input Value")
except FileNotFoundError:
	exit(f"\n[>>] File " + x + "Not Found")
print("")
l = open(u, 'w')
l.write(t)
l.close()
print("\n[>>] Your Encoded File Save As >> \x1b[1;92m" + u )
exit()


