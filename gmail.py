# Tutorial at https://realpython.com/python-send-email/

import smtplib, ssl

import gmail_account_details

port = 465  # For SSL


def send_mail(recip, subj, body):
    message = 'Subject: {}\n\n{}'.format(subj, body)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(gmail_account_details.email, gmail_account_details.password)
        server.sendmail(gmail_account_details.email, recip, message)


send_mail("wpbdry@gmail.com", "subject text", "hello")
