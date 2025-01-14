import smtplib
import ssl
from email.message import EmailMessage


def send_email(subject, html, to_email, from_email, password):
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email
    message.add_alternative(html, subtype='html')
    # message.set_content(body)

    context = ssl.create_default_context()
    print("Sending email...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent!")
    

subject = "Test"
body = "This is a test"
html = f'''
<h1>{{subject}}</h1>
<p>{{body}}</p>
'''
sender_email = "first@gmail.com"
receiver_email = "dan646655@gmail.com@gmail.com"
password = input("Type your password and press enter:")
send_email(subject, html, receiver_email, sender_email, password)