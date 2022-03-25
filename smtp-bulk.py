from email import message
import smtplib, ssl
from time import strftime
import time
from random import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.headerregistry import Address
from email.header import Header
import smtplib
import colorama
from colorama import Fore
from colorama import *
from datetime import datetime
from datetime import date
import os
import platform
platform.system()
if platform.system() == 'Linux':

    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')    


#Took me 2 hours to get this shit done so unless u are adding some stuff dont fucking touch a shit

today = date.today()
print(Fore.RED + f"""
        
                             SMTP Bulk Sender v 1.0.0        Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap                                                 """)

try:
    context = ssl.create_default_context()

#variables tawa3na :
    print(f'\n[+]SETUP SMTP SERVER FIRST : ')
    smtp_server = input('Enter your smtp server HOST: ')
    smtp_port = input('Enter your SMTP port :')
    smtp_user = input('Please enter your SMTP USERNAME : ')
    smtp_pass = input('Enter your SMTP password : ')
    clear()
    print(Fore.RED +f"""
        
                             SMTP Bulk Sender v 1.0.0        Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap                                                 """)
    print(f'\n NOW THE LETTER PARTS : ')
    letter_subject = input(' Subject of letter : ')
    letter_path = input('Please Enter PATH TO letter HTML.txt : ')
    letter_From = input('Enter Letter FROM Name  ( EX: Support )  : ')
except KeyboardInterrupt:
    print("\nCTRL+C Detect, leaving :D")
    exit() 
#Fuction lewla njibou les emails men txt

def get_contacts(filename):
    
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
    return emails

mails = get_contacts(input('Enter Path To Mail List (PLEASE FILTER YOUR MAIL LIST) : '))

clear()

print(Fore.GREEN + f"""
        
                             SMTP Bulk Sender v 1.0.0        Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap                                                \n """)


print(Fore.GREEN +'''##########################SENDING DONT PANIC###############################''')


#2eme function de send
def generate_messages(recipients):
    with open(letter_path, 'r') as myfile:
        data = myfile.read()

    for recipient in recipients:
        message = EmailMessage()
        message['Subject'] = letter_subject
        message['From'] = Address(letter_From, *smtp_user.split("@"))
        message['To'] = recipient
        message.set_content(data, 'html')                
        yield message



def smtp(smtp_server, port, user, password, messages):
  try:

    if port == '587':
        
            with smtplib.SMTP(smtp_server, port) as server:
                 
                try:
                 
                     server.login(user, password)
                     print(Fore.GREEN +
                     f'''\n\n\nSMTP CONNECTION ESTABLISHED :\n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n NO CONNECTION ERRORS! \n Wish with me no other erors haha ''')
                     for message in messages:
                         now = datetime.now()
                         time.sleep(5)
                         server.send_message(message)
                
                
                         print(Fore.GREEN +'\n[+]', message['To'] + f''' SENT!  {time.strftime('%X')}''')
                     print(Fore.GREEN +'''\n ###################################################################### SENT''')
                
                     
                 
                    
                except smtplib.SMTPException:
                    print(Fore.RED +'SMTP DIED OR DEAD [-] Error: unable to send email')
    elif port == '465':
            with smtplib.SMTP_SSL(smtp_server, port) as server:
                 
                try:
                 
                    server.login(user, password)
                    print(f'''\n\n\nSMTP CONNECTION ESTABLISHED :\n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n NO CONNECTION ERRORS! \n Wish with me no other erors haha  ''')
                    for message in messages:
                         now = datetime.now()
                         current_time = now.strftime("%H:%M:%S")
                         time.sleep(5)
                         server.send_message(message)
                
                         print(Fore.GREEN +'\n[+]', message['To'] + f''' SENT!  {time.strftime('%X')}''')
                    print(Fore.GREEN +'''\n ###################################################################### SENT''')
                
                
                except smtplib.SMTPException:
                    print(Fore.RED +'SMTP DIED OR DEAD [-] Error: unable to send email')
     
    
    else:
        print('wrong PORT')
  except KeyboardInterrupt:
            print("CTRL+C Detect, leaving :D")
            exit()      

try:
    smtp(smtp_server=smtp_server, port=smtp_port, user=smtp_user,  password=smtp_pass, messages=generate_messages(mails))
except KeyboardInterrupt:
    print('\nCTRL + C DETECTED LEAVING')
    exit()    
