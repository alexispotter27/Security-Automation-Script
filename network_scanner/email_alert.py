import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Configurations
SMTP_SERVER = "smtp.gmail.com"  # Change if using Outlook/Yahoo
SMTP_PORT = 587
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Use App Password for security
EMAIL_RECEIVER = "receiver-email@example.com"

def send_email_alert(subject, message):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("[✅] Email alert sent successfully!")
    except Exception as e:
        print(f"[❌] Error sending email: {e}")

# Example Usage
if __name__ == "__main__":
    send_email_alert("Security Alert 🚨", "Unauthorized device detected!")
