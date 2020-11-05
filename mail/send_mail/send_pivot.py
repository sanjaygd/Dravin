import imghdr
import os
import smtplib
from email.message import EmailMessage



EMAIL_ADDRESS = os.environ.get("USER_MAIL_ID")
EMAIL_PASSWORD = os.environ.get("USER_PASSWORD")
contacts = ['sanjaygd35@gmail.com','sanjaygd96@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Sent it again'
msg['From'] = EMAIL_ADDRESS
msg['To']  = 'sanjaygd96@gmail.com'  # To send single user
# msg['To'] = ','.join(contacts)  #To send multiple user
msg.set_content("Message content changed...!")


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)

print('Message Sent...!')

