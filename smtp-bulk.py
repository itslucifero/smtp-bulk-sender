import smtplib, ssl
from time import strftime
import time
from random import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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


context = ssl.create_default_context()

def smtp(smtp_server, port, user, password):
    
    if port == '587':
        
        with smtplib.SMTP(smtp_server, port) as server:
            try:
                 
                 html = open(letter_path, 'r')
                 data = html.read()
                 message = MIMEMultipart('alternative')
                 message['Subject'] = letter_subject
                 message['From'] = str(Header(f'{letter_From} <{smtp_user}>'))
                 
                 part1 = MIMEText(data, 'html')
                 message.attach(part1)


                 server.ehlo()  
                 server.starttls()
                 server.ehlo()  
                 server.login(user, password)
                 
                 print(f'''\n\n\nSMTP ALIVE :\n SERVER : {smtp_server}\n User: {user}\n Pass: {password}\n PORT : {port} \n MESSAGE SENT! ''')
                 print('''\n ###################################################################### SENT''')
                 for email in mails:
                    print('\n',email + f''' SENT!  {time.strftime('%X')}''')
                    message['To'] = email
                    server.sendmail(user, mails, message.as_string())
            except smtplib.SMTPAuthenticationError or smtplib.SMTPConnectError or smtplib.SMTPDataError :
                 print('Dead SMTP CHANGE IT')    
    elif port == '465':
        with smtplib.SMTP_SSL(smtp_server, port) as server:
           
            try:
                
                 html = open(letter_path, 'r')
                 data = html.read()
                 message = MIMEMultipart('alternative')
                 message['Subject'] = letter_subject
                 message['From'] = str(Header(f'{letter_From} <{smtp_user}>'))
                 
                 
                 
                 
                 part1 = MIMEText(data, 'html')
                 message.attach(part1)
                 
                 now = datetime.now()
                 current_time = now.strftime("%H:%M:%S")
   
                 server.login(user, password)
                
                 print(f'''\n\n\n----------SMTP ALIVE : {current_time} \n----------SERVER : {smtp_server}\n----------User: {user}\n----------Pass: {password}\n----------PORT : {port} \n----------MESSAGE SENT! ''')
                 print('''\n###################################################################### SENT''')
                 for email in mails:
                    print('\n',email + f''' SENT! {time.strftime('%X')}''')
                    message['To'] = email
                    server.sendmail(user, mails, message.as_string())
            except smtplib.SMTPAuthenticationError or smtplib.SMTPConnectError or smtplib.SMTPDataError :
                 print('Dead SMTP CHANGE IT')    

    else:
        print('PORT NOT SUPPORTED')
        quit()
    


smtp(smtp_server=smtp_server, port=smtp_port, user=smtp_user,  password=smtp_pass)