import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_log_email():
    fromaddr = 'ksenikrsk@mail.ru'
    toaddr = 'ksenikrsk@mail.ru'
    mypass = 'fNULqzW7qaaucyPuhsgh'
    reportname = 'log.txt'

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Отчет о тестировании'

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part[
            'Content-Disposition'] = 'attachment; filename=%s"' % basename(
            reportname)
        msg.attach(part)

    body = "Автоматический отчет об тестировании"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    send_log_email()



