import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage() ## Set the msg variablee as an EmailMessage object
    msg.set_content("This is a sample email!")
    msg["Subject"] = "SAMPLE SAMPLE"
    msg["From"] = "youremail@gmail.com"
    msg["To"] = "receipient@gmail.com"

    ## connecting to gmail servers

    with smtplib.SMTP_SSL("smtp.gmail.com", 465 ) as server:
        server.login("youremail@gmail.com","APP PASSWORD")
        server.send_message(msg)
    
    print("Program ran successfully")

send_email()