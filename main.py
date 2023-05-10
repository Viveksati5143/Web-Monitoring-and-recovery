import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from time import sleep

# Set the URL of the web application to monitor
app_url = "https://example.com"

# Set the email parameters
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "viveksati001@gmail.com"
receiver_email = "viveksati2002@gmail.com"
email_password = "your_email_password"

def send_notification(subject, body):
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, email_password)
        server.send_message(message)

def check_application():
    try:
        response = requests.get(app_url)
        if response.status_code == 200:
            print(f"[{datetime.now()}] Web application is running.")
        else:
            print(f"[{datetime.now()}] Web application is not running (Status code: {response.status_code}).")
            send_notification("Web Application Down", "The web application is not running.")
            recover_application()
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Web application is not running (Error: {e}).")
        send_notification("Web Application Down", f"The web application is not running. Error: {e}.")
        recover_application()

def recover_application():
    # Implement your recovery logic here
    # For example, you could restart a server or perform any necessary actions to restore the application
    print("Attempting to recover the web application...")
    # Sleep for a few seconds to allow time for recovery
    sleep(5)
    check_application()

# Run the monitoring script continuously
while True:
    check_application()
    # Check the application status every 5 minutes
    sleep(300)
