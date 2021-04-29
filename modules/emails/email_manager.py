import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'epssaludunal@gmail.com'
PASSWORD = 'epssaludunal123'


def send_messages(messages):
    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.ehlo()
    s.login(MY_ADDRESS, PASSWORD)
    
    for name, email, date_time, city in messages:
        msg = MIMEMultipart()
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Programación de Vacunación"

        msg.attach(MIMEText(f"""
            Saludos, {name}.
            Nos complace informarle que su vacunación fue programada para:
            {date_time}
            en {city}.
        """, 'plain'))
        s.send_message(msg)

        del msg