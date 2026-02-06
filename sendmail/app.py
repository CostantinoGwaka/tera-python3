from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template


template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Gwaka"
message["to"] = "gwaka94@gmail.com"
message["subject"] = "Test Email"
body = template.substitute({"name": "Robert Redempta"})
message.attach(MIMEText(body, "plain"))
# message.attach(MIMEImage(Path("python.png").read_bytes(), name="python.png"))


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("robertredempta@gmail.com", "1965Redempta")
    smtp.send_message(message)
    print("Email sent successfully!")

# def send_email():
# sender_email = "gwaka94@gmail.com"
# receiver_email = "gwaka94@gmail.com"
# subject = "Test Email"
# body = "This is a test email sent from Python."
# # Create a multipart email message
# msg = MIMEMultipart()
# msg["From"] = sender_email
# msg["To"] = receiver_email
# msg["Subject"] = subject
# # Attach the email body to the message
# msg.attach(MIMEText(body, "plain"))
# # Send the email using SMTP
# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, "your_password")
#         server.send_message(msg)
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Failed to send email: {e}")


# send_email()
