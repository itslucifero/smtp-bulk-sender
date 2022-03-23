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
print(f"""
        
                             SMTP Bulk Sender v 1.0.0        Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap                                                 """)


context = ssl.create_default_context()

#variables tawa3na :
print(f'\n SETUP SMTP SERVER FIRST : ')
smtp_server = input('Enter your smtp server HOST: ')
smtp_port = input('Enter your SMTP port :')
smtp_user = input('Please enter your SMTP USERNAME : ')
smtp_pass = input('Enter your SMTP password : ')
clear()
print(f"""
        
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

#Fuction lewla njibou les emails men txt

def get_contacts(filename):
    
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
    return emails

mails = get_contacts(input('Enter Path To Mail List (PLEASE FILTER YOUR MAIL LIST) : '))

clear()

print(f"""
        
                             SMTP Bulk Sender v 1.0.0        Coded By :       
                                                                                      
██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚══███╔╝
███████║██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║  ███╔╝ 
██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║ ███╔╝  
██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
              Date :  {today}
              Contact : https://t.me/kickflap                                                \n """)


print('''##########################SENDING DONT PANIC###############################''')


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
    
    if port == '587':
        
            with smtplib.SMTP(smtp_server, port) as server:
                 
                try:
                 server.login(user, password)
                 print(f'''\n\n\nSMTP ALIVE :\n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n MESSAGE SENT! ''')
                 for message in messages:
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    server.send_message(message)
                    
                    print('\n',message['To'] + f''' SENT!  {time.strftime('%X')}''')
                 print('''\n ###################################################################### SENT''')
                except smtplib.SMTPAuthenticationError or smtplib.SMTPConnectError or smtplib.SMTPDataError :
                 print('Dead SMTP CHANGE IT')    
    elif port == '465':
            with smtplib.SMTP_SSL(smtp_server, port) as server:
                 
                try:
                 server.login(user, password)
                 print(f'''\n\n\nSMTP ALIVE :\n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n MESSAGE SENT! ''')
                 for message in messages:
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    server.send_message(message)
                
                    print('\n',message['To'] + f''' SENT!  {time.strftime('%X')}''')
                 print('''\n ###################################################################### SENT''')
                
                
                except smtplib.SMTPAuthenticationError or smtplib.SMTPConnectError or smtplib.SMTPDataError :
                 print('Dead SMTP CHANGE IT')    

    else:
        print('PORT NOT SUPPORTED')
        quit()
    


smtp(smtp_server=smtp_server, port=smtp_port, user=smtp_user,  password=smtp_pass, messages=generate_messages(mails))
