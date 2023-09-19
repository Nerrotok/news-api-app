import smtplib
import ssl
import config


def send_email(message):
    host = config.host
    port = config.port
    user_name = config.user_name
    password = config.password
    receiver = config.receiver
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
