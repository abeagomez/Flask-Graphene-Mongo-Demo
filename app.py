# flask_graphene_mongo/app.py
from flask import Flask

from database import init_db
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True

# default_query = '''
# {
#   allEmployees {
#     edges {
#       node {
#         id,
#         name,
#         department {
#           id,
#           name
#         },
#         role {
#           id,
#           name
#         }
#       }
#     }
#   }
# }'''.strip()

init_db()
app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    # init_db()
    app.run()
