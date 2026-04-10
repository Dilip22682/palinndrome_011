import smtplib

# EMAIL = "your_email@gmail.com"
# APP_PASSWORD = "abcdefghijklmnop"
SENDER_EMAIL = "dilipnc222025@gmail.com"
APP_PASSWORD = "zamr bzzj vfjf vppg"  # 16-character App Password

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, APP_PASSWORD)

print("✅ Login successful!")
server.quit()
