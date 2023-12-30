# Server Health Check Script
# Uses psutil library for system information

import psutil
import smtplib
from email.mime.text import MIMEText

def check_server_health():
    # Get system information
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Customize threshold values as needed
    if cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
        send_email_alert(f"Server Alert - High Resource Usage\n\nCPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}%\nDisk Usage: {disk_usage}%")

def send_email_alert(message):
    # Send email using SMTP
    # Make sure to set up SMTP configuration
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    receiver_email = 'admin@example.com'
    password = 'your_email_password'

    msg = MIMEText(message)
    msg['Subject'] = 'Server Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    check_server_health()
