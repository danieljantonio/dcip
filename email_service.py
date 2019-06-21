import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from time import asctime, localtime
import getpass


def send_email(receiver_email, flagged_text, filename):
    # email information and smtp server setup
    port = 465 # for SSL
    password = "D4mG4482"
    smtp_server = "smtp.gmail.com"
    sender_email = "unbullymy@gmail.com"
    receiver_name = getpass.getuser()
    message = MIMEMultipart("alternative")
    message["Subject"] = "Cyberbullying Flag!"
    message["From"] = sender_email
    message["To"] = receiver_email

    # message body
    body = """
    <html>
        <body>
            <h2> Potential cyberbullying detected in """ + receiver_name + """'s device </h2>
            <p>Notice: Your child may be involved or may have witnessed cyberbullying in his device.</p>
            <p>Contents that have been flagged by our system: </p>
            <ul>"""

    # inserting flagged text into unordered list
    for text in flagged_text:
        body = body + "<li>" + text + "</li>"

    body = body + """
            </ul>
            <i> Please review it on the file attached in this email and deal with it appropriately with love and care.</i>
        </body>
    </html>"""

    # attaching the html body to the email
    html_content = MIMEText(body,"html")
    message.attach(html_content)

    # attaching the screenshot containing the profanity 
    file_directory = ".cache/" + str(filename) + ".jpg"
    screenshot_time = asctime(localtime(filename))
    with open(file_directory, "rb") as attachment:
        attachment_image = MIMEImage(attachment.read())

    # naming the image 
    attachment_image.add_header(
        "Content-Disposition",
        f"attachment; filename=" + str(screenshot_time) + ".jpg",
    )

    # attach the image
    message.attach(attachment_image)

    # generate ssl context
    context = ssl.create_default_context()

    # send email from the smtp server
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
