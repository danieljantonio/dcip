import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, receiver_name, flagged_text):
    port = 465 # for SSL
    password = "D4mG4482"
    smtp_server = "smtp.gmail.com"
    sender_email = "unbullymy@gmail.com"
    receiver_email = "djedidiaha@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Cyberbullying Flag!"
    message["From"] = sender_email
    message["To"] = receiver_email


    html = """
    <html>
        <body>
            <h2> Potential cyberbullying detected in """ + receiver_name + """'s device </h2>
            <p>Contents that have been flagged by our system: </p>
            <ul>"""

    for text in flagged_text:
        html = html + "<li>" + text + "</li>"

    html = html + """
            </ul>
            <i> Please review it on the file attached in this email and deal with it appropriately </i>
        </body>
    </html>"""
    html_content = MIMEText(html,"html")
    message.attach(html_content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# send_email("djedidiaha@gmail.com", 'Daniel Antonio', ['fuck you', 'you fuck'])