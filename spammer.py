import smtplib
import imghdr
from email.message import EmailMessage

email = "aovil420@gmail.com"
password = ""
receiver = "aovil420@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Chin Chin"
msg["From"] = email
msg["To"] = receiver
msg.set_content("Our lord and savior!")

with open("chin_chin.png", "rb") as p:
    f = p.read()
    f_type = imghdr.what(p.name)
    f_name = p.name

msg.add_attachment(f, maintype="image", subtype=f_type, filename=f_name)

with smtplib.SMTP_SSL("smptp.gmail.com", 465) as smtp:
  smtp.login(email, password)
  for i in range(1, 25):
    smtp.send_message(msg)
