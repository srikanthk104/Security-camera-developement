  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# Email you want to send the update from (only works with gmail)
fromEmail = 'srikanth.k104@gmail.com'
# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
fromEmailPassword = '9421717901'

# Email you want to send the update to
toEmail = 'srikanth.k86894@gmail.com'

def sending(frame):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Security Update'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'Raspberry pi security camera update'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('Smart security cam found object')
    msgAlternative.attach(msgText)
    msgText = MIMEText('<img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)
    fp=frame
    msgImage = MIMEImage(fp)
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()