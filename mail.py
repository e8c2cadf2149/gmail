import smtplib
import time

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('Your_Email', 'Your-Password')
SUBJECT = 'This  Project is under development '
s = time.strftime("%Y-%b-%d %I:%M")
TEXT =  s, ' Testing for the parameters'





message = f'Subject: {SUBJECT}\n\n{TEXT}'
while True:
    server.sendmail(f'testpyhton11@gmail.com', 'Reciever's_Email', message)
    print("Mail sent at :", s)
    time.sleep(1200)




