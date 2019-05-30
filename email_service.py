import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from time import asctime, localtime


def send_email(receiver_email, receiver_name, flagged_text, filename):
    port = 465 # for SSL
    password = "D4mG4482"
    smtp_server = "smtp.gmail.com"
    sender_email = "unbullymy@gmail.com"
    receiver_email = "djedidiaha@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Cyberbullying Flag!"
    message["From"] = sender_email
    message["To"] = receiver_email


    body = """
    <html>
        <body>
            <h2> Potential cyberbullying detected in """ + receiver_name + """'s device </h2>
            <p>Contents that have been flagged by our system: </p>
            <ul>"""

    for text in flagged_text:
        body = body + "<li>" + text + "</li>"

    body = body + """
            </ul>
            <i> Please review it on the file attached in this email and deal with it appropriately </i>
        </body>
    </html>"""
    html_content = MIMEText(body,"html")
    message.attach(html_content)
    file_directory = ".cache/" + str(filename) + ".jpg"
    screenshot_time = asctime(localtime(filename))
    with open(file_directory, "rb") as attachment:
        attachment_image = MIMEImage(attachment.read())
        # part = MIMEBase("application", "octet-stream")
        # part.set_payload(attachment.read())
    
    # encoders.encode_base64(part)
    attachment_image.add_header(
        "Content-Disposition",
        f"attachment; filename=" + str(screenshot_time) + ".jpg",
    )
    message.attach(attachment_image)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# send_email("djedidiaha@gmail.com", 'Daniel Antonio', ['fuck you', 'you fuck'], 1559188405)