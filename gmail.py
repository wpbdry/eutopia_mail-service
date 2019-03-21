# Tutorial at https://realpython.com/python-send-email/

import smtplib, ssl

import config

port = 465  # For SSL
fromAddr = config.gmail_email


def send_mail(recip, subj, body):
    message = 'To: {}\nFrom: {}\nSubject: {}\n\n{}'.format(recip, fromAddr, subj, body)

    # Create a secure SSL context
    context = ssl.create_default_context()


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(config.gmail_email, config.gmail_password)
            server.sendmail(fromAddr, recip, message)
            return {
                "ok": True,
                "msg": "Successful!"
            }
    except Exception as e:
        return {
            "ok": False,
            "msg": str(e)
        }
