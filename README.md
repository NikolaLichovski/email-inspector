# Email Inspector

A straightforward Python tool to send a test email and scan your most recent inbox messages for spam keywords using IMAP and SMTP.

---

## Features

- Sends a test email with SMTP using your credentials.
- Connects to your inbox via IMAP and fetches only the 10 most recent emails for scanning.
- Detects potential spam by searching for suspicious keywords in both the email subject and body.
- Loads spam keywords from an external file (`spam_keywords.txt`), with a sensible default list if none is provided.
- Logs all actions and spam detections to a local file for later review.
- Fully configurable via command-line arguments.
- Securely prompts for passwords at runtime without exposing credentials.

---

## Requirements

- Python 3.6 or newer.
- Uses only standard Python libraries:
  `imaplib`, `email`, `smtplib`, `argparse`, `getpass`, `logging`.

---

## Usage

Send a test email and scan your inbox in one go:

    python email_inspector.py \
      --imap-server imap.example.com \
      --email-user your.email@example.com \
      --smtp-server smtp.example.com \
      --smtp-port 587 \
      --sender-email your.email@example.com \
      --recipient-email recipient@example.com

To scan your inbox without sending a test email:

    python email_inspector.py \
      --imap-server imap.example.com \
      --email-user your.email@example.com

The script will prompt you securely for the required IMAP and SMTP passwords when needed.

---

## Command-Line Arguments

| Argument            | Description                                         | Required / Default        |
|---------------------|-----------------------------------------------------|---------------------------|
| `--imap-server`     | IMAP server address (e.g., `imap.gmail.com`)        | Required                  |
| `--email-user`      | Email address for fetching emails via IMAP          | Required                  |
| `--smtp-server`     | SMTP server address (e.g., `smtp.gmail.com`)        | Optional (default: Gmail) |
| `--smtp-port`       | SMTP port (typically 587)                           | Optional (default: 587)   |
| `--sender-email`    | Email address to send the test email from           | Optional                  |
| `--recipient-email` | Email address to receive the test email             | Optional                  |

---

## How It Works

1. **Send a test email** (if sender and recipient are provided) using SMTP with credentials entered securely at runtime.  
2. **Connect to your inbox via IMAP** and fetch only the 10 most recent emails.  
3. **Scan both subject lines and email bodies** for spam keywords loaded from a configurable file or default list.  
4. **Log all activity and detected spam** into `email_inspector.log` for review.

---

## Spam Detection

Spam detection is based on simple keyword matching within email subjects and bodies. The keywords are loaded from a file named `spam_keywords.txt` (one keyword per line). If this file is not found, the tool uses a default list including:

- win  
- prize  
- free  
- lottery  
- money  
- urgent

---

## Using With Popular Email Providers

### Gmail

- **IMAP server:** `imap.gmail.com`  
- **SMTP server:** `smtp.gmail.com`  
- **Port:** 587  
- **Important:** Use an **App Password** (not your regular Gmail password).  
  - Enable 2-Step Verification: https://myaccount.google.com/security  
  - Generate App Password: https://myaccount.google.com/apppasswords  
  - Use this app password when prompted by the script.

More info: https://support.google.com/mail/answer/185833

---

### Outlook / Hotmail / Microsoft 365

- **IMAP server:** `imap-mail.outlook.com`  
- **SMTP server:** `smtp-mail.outlook.com`  
- **Port:** 587  
- May require an **App Password** if 2FA is enabled.  
  - Setup guide: https://support.microsoft.com/en-us/account-billing/create-app-passwords-to-sign-in-to-apps-using-two-step-verification-7307c836-3bd3-4c93-9f07-50f3439a3f83

---

### Yahoo Mail

- **IMAP server:** `imap.mail.yahoo.com`  
- **SMTP server:** `smtp.mail.yahoo.com`  
- **Port:** 587  
- **Must use an App Password.**  
  - 2FA and app password setup: https://help.yahoo.com/kb/SLN15241.html

---

### Proton Mail

Proton Mail does not support direct IMAP/SMTP access due to end-to-end encryption. Use ProtonMail Bridge instead:

- Download ProtonMail Bridge: https://proton.me/mail/bridge  
- Use the local IMAP/SMTP details provided by the Bridge:  
  - Usually `127.0.0.1` on ports `1143` (IMAP) and `1025` (SMTP).  
- Use Bridge credentials when prompted by the script.  
- Ensure the Bridge app is running while using the script.

---

## Example: Gmail

    python email_inspector.py \
      --imap-server imap.gmail.com \
      --email-user myemail@gmail.com \
      --smtp-server smtp.gmail.com \
      --smtp-port 587 \
      --sender-email myemail@gmail.com \
      --recipient-email someone@example.com

Enter your Gmail **App Password** when prompted.

---

## License

Provided as-is for educational and non-commercial use.

---
