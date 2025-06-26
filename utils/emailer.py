import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body, smtp_server="smtp.example.com", port=587, sender="noreply@example.com", password="your_password"):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)