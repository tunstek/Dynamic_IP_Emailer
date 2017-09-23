import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText



# **** ENTER THE FOLLOWING DETAILS ****
mail_server_username = ""
mail_server_password = ""
sender_email = ""
receiver_email = ""


def send_alert(subject, body):


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    message = body
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp1r.cp.blacknight.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(mail_server_username, mail_server_password)

    mailserver.sendmail(sender_email,receiver_email,msg.as_string())

    mailserver.quit()
