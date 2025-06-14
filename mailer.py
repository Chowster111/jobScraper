# mailer.py
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

class Mailer(object):
    def __init__(self):
        self.fromUser = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASS")
        self.toUser = os.getenv("EMAIL_TO")

        if not all([self.fromUser, self.password, self.toUser]):
            raise EnvironmentError("Missing EMAIL_USER, EMAIL_PASS, or EMAIL_TO in .env")
    def send_email_notification(self, subject, body):
        msg = MIMEText(body, "plain")
        msg["Subject"] = subject
        msg["From"] = self.fromUser
        msg["To"] = self.toUser

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.fromUser, self.password)
                server.send_message(msg)
        except Exception as e:
            print("❌ Failed to send email:", e)