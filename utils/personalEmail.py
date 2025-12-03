import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage


def sendmail(email,name):
    load_dotenv()
    msg = EmailMessage()
    msg["Subject"] = "Test Message"
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = email
    msg.set_content(f"HI {name} i would like you to make an interview offer")
    #print("smtpUSer", os.getenv("SMTP_USER"))
    with smtplib.SMTP(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.send_message(msg)
