import smtplib

mailFrom = "Your automation system"
mailTo = ["damiankrata92@tlen.pl", "ola-kudla@wp.pl"]
mailSubject = "Processing finished succerssfull"
mailBody = '''Hello
kocham Cie Olcia
mrrr'''
message = '''From: {}
Subject:{}
{}
'''.format(mailFrom, mailSubject, mailBody)

user = "damiankrata92@gmail.com"
password = '92090313551'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print("mail sent")
except:
    print("Error sending mail")
