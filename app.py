from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///lahmansbaseballdb.sqlite')

app = Flask(__name__)
api = Api(app)

class Parks_Meta(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from parks;")
        return {'parks': [i for i in query.cursor.fetchall()]}

api.add_resource(Parks_Meta, '/parks')

if __name__ == '__main__':
    app.run()
