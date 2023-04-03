import smtplib
import os
from email.mime.text import MIMEText


def send_email(message):
    sender = "slessarevalex@gmail.com"
    reciever = "slessarevalex@ya.ru"
    reciever_copy= "a.dotsenko@avicentr.ru"
    password = "cltqhljlupwersmr"
    # password = "os.getenv("EMAIL_PASSWORD")"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Парсер категорий отелей"
        server.sendmail(sender, reciever, msg.as_string())
        server.sendmail(sender, reciever_copy, msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


# def main():
#     message = input("Type your message: ")
#     print(send_email(message=message))


# if __name__ == "__main__":
#     main()
