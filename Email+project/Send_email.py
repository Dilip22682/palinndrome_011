import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =========================
# Gmail Login Details
# =========================
SENDER_EMAIL = "dilipnc222025@gmail.com"
APP_PASSWORD = "zamr bzzj vfjf vppg"  # 16-character App Password

# =========================
# Email Content
# =========================
SUBJECT = "Important Update"

EMAIL_TEMPLATE = """
Hello {name},

This is an automated email sent using Python.
Hope you are doing well.

Best regards,
Your Name
"""

# =========================
# Load Excel File
# =========================
df = pd.read_excel("emails.xlsx")

# =========================
# Connect to Gmail SMTP
# =========================
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, APP_PASSWORD)

# =========================
# Send Emails
# =========================
for _, row in df.iterrows():
    name = row["Name"]
    email = row["Email"]

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = email
    message["Subject"] = SUBJECT

    body = EMAIL_TEMPLATE.format(name=name)
    message.attach(MIMEText(body, "plain"))

    server.sendmail(SENDER_EMAIL, email, message.as_string())
    print(f"✅ Email sent to {name} ({email})")

server.quit()
print("\n🎉 All emails sent successfully!")
