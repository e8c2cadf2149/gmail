import smtplib
import time

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('testpyhton11@gmail.com', 'e8c2cadf2149')
SUBJECT = 'This  Project is under development '
TEXT = ' Testing.'

message = f'Subject: {SUBJECT}\n\n{TEXT}'
server.sendmail(f'testpyhton11@gmail.com', 'gautambisht709@gmail.com', message)

