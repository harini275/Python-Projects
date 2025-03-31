import smtplib
to=input('Enter the email of recipent:\n')
content=input("Enter the content for email:\n")
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('sender2gmail.com',to,content)
    server.close()
sendEmail(to,content)    