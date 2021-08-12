import smtplib

from email.mime.text import MIMEText
from email.header import Header

import schedule

charset = 'utf-8'


# def prompt(prompt):
#     return input(prompt).strip()

fromaddr = "matsuokuniko7@gmail.com"
toaddr  = "matsuokuniko7+1@gmail.com" #fromとtoが同じアドレスの書き方
# print("Enter message, end with ^D (Unix) or ^Z (Windows):")

## Add the From: and To: headers at the start!
# msg = ("From: %s\r\nTo: %s\r\n\r\n"
#       % (fromaddr, toaddr))
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     if not line:
#         break
#     msg = msg + line

# print("Message length is", len(msg))

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
# gmailとgmailのパスワード2段階認証
server.login('matsuokuniko7@gmail.com','nkuemwjezyhnogiv')
server.set_debuglevel(1)

users = [
    {'name':'松尾一郎','address':'matsuokuniko7+1@gmail.com'},
    {'name':'松尾二郎','address':'matsuokuniko7+2@gmail.com'},
    {'name':'松尾三郎','address':'matsuokuniko7+3@gmail.com'},
]

for user in users:
    content = f'''
        {user["name"]}さん
        
        こんにちは。
        この度はお世話になりました。
    '''
    message = MIMEText(content, 'plain', charset)
    message['Subject'] = Header('題名'.encode(charset), charset) 
    
    
    server.sendmail(fromaddr, user['address'], message.as_string())
server.quit()