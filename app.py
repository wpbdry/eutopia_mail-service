from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

import schema

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule(
    '/send-mail',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema.schema,
        graphiql=True, # GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()
