import smtplib
import time

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('testpyhton11@gmail.com', 'e8c2cadf2149')
SUBJECT = 'This  Project is under development '
s = time.strftime("%Y-%b-%d %I:%M")
TEXT =  s, ' Testing for the parameters'





message = f'Subject: {SUBJECT}\n\n{TEXT}'
while True:
    server.sendmail(f'testpyhton11@gmail.com', 'gautambisht709@gmail.com', message)
    print("Mail sent at :", s)
    time.sleep(12)




