from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, bindparam
from json import dumps

e = create_engine('sqlite:///lahmansbaseballdb.sqlite')
metadata = MetaData()
parks = Table('parks', metadata, autoload=True, autoload_with=e)
teams = Table('teams', metadata, autoload=True, autoload_with=e)


app = Flask(__name__)
api = Api(app)

class All_Parks(Resource):
    def get(self):
        conn = e.connect()
        query = select([parks])
        res = conn.execute(query)
        headers = [x for x in res.keys()]
        json_data = []
        for r in res:
            json_data.append(dict(zip(headers,r)))
        json_data = { 'parks': json_data }
        return {'status': "success", 'data': json_data}


class All_Teams(Resource):
    def get(self):
        conn = e.connect()
        query = select([teams])
        res = conn.execute(query)
        headers = [x for x in res.keys()]
        json_data = []
        for r in res:
            json_data.append(dict(zip(headers,r)))
        json_data = { 'teams': json_data }
        return {'status': "success", 'data': json_data}

class Teams_By_Name(Resource):
    def get(self, franchID: str):
        conn = e.connect()
        query = teams.select(teams.c.franchID.ilike(bindparam('franchID')))
        # https://docs.sqlalchemy.org/en/13/core/tutorial.html#bind-parameter-objects
        res = conn.execute(query, franchID=franchID)
        headers = [x for x in res.keys()]
        json_data = []
        for r in res:
            json_data.append(dict(zip(headers,r)))
        return {'teams': [json_data]}

api.add_resource(All_Parks, '/parks')
api.add_resource(All_Teams, '/teams')
api.add_resource(Teams_By_Name, '/team/<string:franchID>')

if __name__ == '__main__':
    app.run()
