import smtplib


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('testpyhton11@gmail.com', 'e8c2cadf2149')
abc = 'full'
server.sendmail('testpyhton11@gmail.com', 'gautambisht709@gmail.com', abc)
print('mail was sent')
server.quit() 