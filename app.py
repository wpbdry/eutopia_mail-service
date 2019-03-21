from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

import sendmail_schema as sendmail

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule(
    '/send-mail',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=sendmail.schema,
        graphiql=True, # GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()
