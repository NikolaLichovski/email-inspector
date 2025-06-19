import smtplib
from email.mime.text import MIMEText
import logging

def send_test_email(smtp_server, smtp_port, sender_email, recipient_email, password):
    """
    Sends a simple test email via SMTP using provided credentials.
    """
    msg = MIMEText("This is a test email from Email Inspector.")
    msg['Subject'] = 'Test Email from Email Inspector'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        logging.info(f"Sent test email from {sender_email} to {recipient_email}")
        print("Test email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        print("Failed to send test email. See log for details.")
