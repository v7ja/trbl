import requests 
import random,datetime,sys,pyfiglet

ab = '\033[1;34m'
ood = pyfiglet.figlet_format(' cLimer v3 ')
print(ab+ood)




Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="_._._._._."

#-------------------------start code ---------------------------#
def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(f"{W}[:] ErRoR uSeR : {user}")
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(f"{Z}[-] BaD uSeR : {user}")
    else:
        email=0
        print(f"{F}[+] GooD uSeR :  {user}")
        email+=1
        god=f"""Nigga iam Here| @{user} | After : 02628"""
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def users():
    ran1="qwertyuiopasdfghjklzxcvbnm1234567890"
    while True:
         v1 = str(''.join((random.choice(insta) for i in range(1))))
         v2 = str(''.join((random.choice(insta) for i in range(1))))
         v3 = str(''.join((random.choice(insta) for i in range(1))))
         v4 = str(''.join((random.choice(insta) for i in range(1))))
         v5 = str(''.join((random.choice(all) for i in range(1))))
         user1 = (v1+v1+v1+v1+v2)
         user2 = (v1+v1+v1+v2+v1)
         user3 = (v1+v1+v2+v1+v1)
         user4 = (v1+v2+v1+v1+v1)
         user5 = (v1+'_'+v2+'_'+v1)
         user6 = (v1+v1+v1+v2+'_')
         user7 = (v3+v3+v1+'_'+v1)
         user8 = (v1+v2+v4+v5)
         user9 = (v1+v2+v1+v1+v2)
         user10 = (v1+v1+v1+'_'+v2)
         user11 = (v1+v1+v1+'.'+v2)
         user12 = (v1+v1+v1+v1+v1+v2)
         user13 = (v2+v1+v1+v1+v1+v1)
         user14 = ('_'+v1+v1+v1+v1)
         user15 = ('.'+v1+v1+v1+v1)
         user16 = ('.'+v2+v1+v1+v1)
         user17 = ('_'+v2+v1+v1+v1)
         user18 = (v1+'.'+v1+'.'+v1)
         user19 = (v1+'_'+v1+'_'+v1)
         user20 = (v2+'.'+v1+'.'+v1)
         user21 = (v2+'_'+v1+'_'+v1)
         user22 = (v2+'.'+v2+'.'+v1)
         user23 = (v2+'_'+v2+'_'+v1)
         user24 = (v1+'_'+v2+'_'+v3)
         user25 = (v1+'.'+v2+'.'+v3)
         user26 = (v1+v1+v1+v1+v1+v1)
         user27 = (v1+v1+v1+v1+v1)
         user28 = (v1+v1+'.'+v1+v1)
         user29 = (v1+v1+'_'+v1+v1)
         user30 = (v1+v2+'.'+v2+v1)
         user31 = (v1+v2+'_'+v2+v1)
         user32 = (v2+v1+'.'+v1+v1)
         user33 = (v2+v1+'_'+v1+v1)
         user34 = (v2+v2+v2+'_'+v1)
         user35 = (v1+v1+v1+'_'+v2)
         abd = (user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14, user15, user16, user17, user18, user19, user20, user21, user22, user23, user24, user25, user26, user27, user28, user29, user30, user31, user32, user33, user34, user35)
         user = random.choice(abd)
         instaa(user)
id=input(f"EnTeR iD : ")
token=input(f"EnTeR ToKeN : ")
print()	
users()
