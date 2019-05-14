# Mail service

This service can receive a GraphQL mutation,
containing email recipient, subject, and body.
The service then sends the specified email using gmail.


### Installation

Edit `secret.py` to look like:
```python
gmail_password_eutopiaplatform = "my_secret"
mail_service_password = "very secret"
```
Edit `config.py` to match your configuration.

Run:
```commandline
$: pip install -r requirements.txt
$: python3 app.py
```

### Usage

The following mutation will then be available at
`localhost:5001/send-mail`


Send emails with queries like the following:
```gql
mutation {
  sendMail(
    recipient: "recipient@mail.tld",
    subject: "Your Email",
    body: "Hello Recipient!",
    password: "very secret"
  ) {
    exitcode
    msg
  }
}
```

#### Exit codes

0: Email sent successfully.

2: Mail service authentication error.
I.e. `password` does not match
`mail_service_password` in `secret.py

3: Error sending email with `smtplib.SMTP_SSL`.
Read `msg` for more details