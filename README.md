# Mail service

This service can receive a GraphQL mutation,
containing email recipient, subject, and body.
The service then sends the specified email using gmail.

### Installation
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
    password: "password"
  ) {
    ok
    msg
  }
}
```