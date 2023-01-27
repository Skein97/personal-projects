import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# not sure of its effect

sender_email_address = input('Enter your Email Address: ')
password = input('Password: ')
receiver_email_address = input("Enter receiver\'s Email Address: ")
server = input('server name: ')
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = input('Enter sender name: ')
email['to'] = receiver_email_address
email['subject'] = 'Email test'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host=server, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email_address, password)
    smtp.send_message(email)
    print('All good')
