import argparse
from getpass import getpass
from mailer import send_test_email
from spam_checker import fetch_and_detect_spam
from utils import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Email Inspector: Send test email & detect spam in inbox")

    # SMTP arguments
    parser.add_argument('--smtp-server', default='smtp.gmail.com', help='SMTP server address (default: smtp.gmail.com)')
    parser.add_argument('--smtp-port', type=int, default=587, help='SMTP server port (default: 587)')
    parser.add_argument('--sender-email', help='Sender email address for sending test email')
    parser.add_argument('--recipient-email', help='Recipient email address for sending test email')

    # IMAP arguments
    parser.add_argument('--imap-server', required=True, help='IMAP server address (e.g., imap.gmail.com)')
    parser.add_argument('--email-user', required=True, help='Email address for fetching emails')

    args = parser.parse_args()

    # Get passwords securely
    smtp_password = None
    if args.sender_email:
        smtp_password = getpass(f"Enter password for SMTP user {args.sender_email}: ")
    imap_password = getpass(f"Enter password for IMAP user {args.email_user}: ")

    # Send test email if details provided
    if args.sender_email and args.recipient_email:
        send_test_email(
            smtp_server=args.smtp_server,
            smtp_port=args.smtp_port,
            sender_email=args.sender_email,
            recipient_email=args.recipient_email,
            password=smtp_password
        )

    # Fetch inbox and detect spam
    fetch_and_detect_spam(
        imap_server=args.imap_server,
        email_user=args.email_user,
        password=imap_password
    )

if __name__ == "__main__":
    main()
