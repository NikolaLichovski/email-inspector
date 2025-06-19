import imaplib
import email
import logging
from utils import decode_subject, load_spam_keywords, extract_body

def fetch_and_detect_spam(imap_server, email_user, password, keywords_file='spam_keywords.txt'):
    """
    Logs in to the IMAP server and scans the last 10 email subjects and bodies for spam keywords.
    """
    spam_keywords = load_spam_keywords(keywords_file)

    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_user, password)
        mail.select('inbox')

        status, messages = mail.search(None, 'ALL')
        if status != 'OK':
            print("Failed to retrieve emails.")
            return

        email_ids = messages[0].split()
        total_emails = len(email_ids)
        logging.info(f"Fetched {total_emails} emails from {email_user}")
        print(f"Found {total_emails} emails in inbox.")

        # Fetch only last 10 emails or fewer if inbox smaller
        last_10_ids = email_ids[-10:]

        for e_id in last_10_ids:
            status, msg_data = mail.fetch(e_id, '(RFC822)')
            if status != 'OK':
                logging.warning(f"Failed to fetch email ID {e_id.decode()}")
                continue
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = decode_subject(msg)
                    body = extract_body(msg)
                    print(f"Subject: {subject}")
                    # Check spam keywords in subject + body
                    combined_text = (subject + " " + body).lower()
                    if any(keyword in combined_text for keyword in spam_keywords):
                        print("-> Marked as spam (keyword detected)")
                        logging.info(f"Spam detected: {subject}")
                    else:
                        print("-> Not detected as spam")
        mail.logout()

    except Exception as e:
        logging.error(f"Failed to fetch or analyze inbox: {e}")
        print("Error accessing inbox. See log for details.")
