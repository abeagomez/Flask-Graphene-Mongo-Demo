# flask_graphene_mongo/app.py
from flask import Flask, render_template
from flask_cors import CORS
from flask import jsonify
from flask import request
import json

from database import init_db
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

CORS(app, resources={r'/*': {'origin':'*'}})
# default_query = '''
# {
#   allPeople {
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

@app.route("/view")
def view():
    return render_template("index.html")

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return 'pong!'

@app.route('/books', methods=['GET'])
def all_books():
    books = [
        {
            'title': 'On the Road',
            'author': 'Jack Kerouac',
            'read': 'True'
        },
        {
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'author': 'J. K. Rowling',
            'read': 'False'
        },
        {
            'title': 'Green Eggs and Ham',
            'author': 'Dr. Seuss',
            'read': 'True'
        }
    ]
    return jsonify(
        status='success',
        books=books
    )

if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
