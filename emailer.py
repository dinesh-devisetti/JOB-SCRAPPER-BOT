import smtplib
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS, EMAIL_PASSWORD  # TODO: Set these environment variables

def send_email(content: str):
    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = "🧑‍💻 Your Daily Entry‑Level Dev Jobs"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # TODO: Replace with your own email if needed

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
