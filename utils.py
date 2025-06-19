import logging
from email.header import decode_header

def setup_logging():
    """
    Sets up logging to file with timestamp and level.
    """
    logging.basicConfig(
        filename='email_inspector.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def decode_subject(msg):
    """
    Safely decodes an email subject to a readable string.
    """
    subject, encoding = decode_header(msg.get("Subject", ""))[0]
    if isinstance(subject, bytes):
        try:
            subject = subject.decode(encoding or 'utf-8', errors='ignore')
        except:
            subject = "[Undecodable subject]"
    return subject or "[No Subject]"

def load_spam_keywords(filepath='spam_keywords.txt'):
    """
    Load spam keywords from a text file, one keyword per line.
    Returns default list if file missing.
    """
    try:
        with open(filepath, 'r') as f:
            keywords = [line.strip().lower() for line in f if line.strip()]
        if not keywords:
            raise ValueError("Empty keywords file")
        return keywords
    except Exception as e:
        logging.warning(f"Failed to load spam keywords from {filepath}: {e}")
        # fallback list
        return ['win', 'prize', 'free', 'lottery', 'money', 'urgent']

def extract_body(msg):
    """
    Extract the plain text body from email message.
    """
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    body_bytes = part.get_payload(decode=True)
                    body = body_bytes.decode(part.get_content_charset() or 'utf-8', errors='ignore')
                    break  # Use first plain text part
                except:
                    continue
    else:
        try:
            body_bytes = msg.get_payload(decode=True)
            body = body_bytes.decode(msg.get_content_charset() or 'utf-8', errors='ignore')
        except:
            body = ""
    return body
