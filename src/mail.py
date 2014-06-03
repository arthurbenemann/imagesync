import smtplib

fromaddr = 'arthur.benemann.auto@gmail.com'
toaddrs  = 'arthur@3drobotics.com'

msg = 'Enter you message here'

# Sending the mail  
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('arthur.benemann.auto@gmail.com','1233211233')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()