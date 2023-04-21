import requests
import time
import smtplib
from email.message import EmailMessage

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def send_email_notification(subject, body, sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

if __name__ == "__main__":
    website_url = "https://www.example.com"  # Replace with the website URL you want to monitor
    monitoring_interval = 60  # Set the monitoring interval in seconds
    sender_email = "sender@example.com"  # Replace with your email address
    recipient_email = "recipient@example.com"  # Replace with the email address to receive notifications
    smtp_server = "smtp.example.com"  # Replace with the SMTP server hostname
    smtp_port = 587  # Replace with the SMTP server port
    smtp_username = "your_smtp_username"  # Replace with your SMTP username
    smtp_password = "your_smtp_password"  # Replace with your SMTP password

    while True:
        if check_website(website_url):
            print(f"{website_url} is up")
        else:
            subject = f"{website_url} is down"
            body = f"{website_url} is currently down. Please investigate."
            send_email_notification(subject, body, sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password)
            print(f"Notification sent: {subject}")

        time.sleep(monitoring_interval)
