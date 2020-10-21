# PeopleData
# Download the .csv file.

# Exercise1:
# 1) Create a python notebook, and make the proper setup with pandas/numpy & sqlalchemy, to persist all 200 people from the .csv file.
# 2) Make a simple flask server with one, get endpoint /flask_app/.
# a) Make it write Hello World.
# 3) Use the Flask extended start code from day 08-2 Web services, and make the following endpoints:
# a)    /api/showAll
# b)    /api/employee/<string: firstName>/<string: lastName>
# c)    /api/employee/add
# d)    /api/employee/delete
# e)    /api/employee/update
# 4) Test endpoints in Postman. 5) Test the class from the .py file in CLI.

# Made by:
# Lucky drawing

# 2)
from flask import Flask, jsonify, abort, request
from sqlalchemy.types import Integer, Text
import sqlalchemy as s_a
import pandas as pd


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/flask_app/')
def index():
    return "Hello, World from flask server!"


# GET #################################################################################


@ app.route('/api/showAll', methods=['GET'])
# 3) a) /api/showAll
def get_all_people():
    result = getFromDB('select * from Week8People')
    return result.to_html()


@ app.route('/api/employee/<string:firstName>/<string:lastName>', methods=['GET'])
# 3) # b)  /api/employee/<string: firstName>/<string: lastName>
def get_task(firstName, lastName):
    result = getFromDB(
        "SELECT * FROM Week8People WHERE `First Name`='{}' AND `Last Name`='{}'"
        .format(firstName, lastName))
    if result.empty:
        abort(404)
    return result.to_html()


def getFromDB(query):
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    sql_df = pd.read_sql(
        query,
        con=engine
    )
    return sql_df


# POST #################################################################################


@ app.route('/api/employee/add', methods=['POST'])
# 3) # c)  /api/employee/add
def create_task():
    if not request.json or not 'First Name' and 'Last Name' in request.json:
        abort(400)
    new_person = {
        "First Name": request.json['First Name'],
        "Last Name": request.json['Last Name'],
        "Gender": request.json['Gender'],
        "Age": request.json['Age'],
        "Email": request.json['Email'],
        "Phone": request.json['Phone'],
        "Occupation": request.json['Occupation'],
        "Salary": request.json['Salary']
    }
    df = pd.json_normalize(new_person)
    addToDB(df)
    return jsonify({"User was added": new_person})


def addToDB(pandasDF):
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    pandasDF.to_sql(
        "Week8People",
        engine,
        if_exists="append",
        index=False,
        dtype={
            "First Name": Text,
            "Last Name": Text,
            "Gender": Text,
            "Age": Integer,
            "Email": Text,
            "Phone": Text,
            "Occupation": Text,
            "Salary": Integer,
        })


# DELETE #################################################################################


@ app.route('/api/employee/delete', methods=['DELETE'])
# 3) # d)  /api/employee/delete
def delete_task():
    if not request.json or not 'First Name' and 'Last Name' in request.json:
        abort(400)
    fName = request.json['First Name']
    lName = request.json['Last Name']
    deleteFromDB(
        "DELETE FROM Week8People WHERE `First Name`='{}' AND `Last Name`='{}'".format(fName, lName))
    return jsonify({"User was deleted": [fName, lName]})


def deleteFromDB(query):
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    conn = engine.connect()
    trans = conn.begin()
    try:
        conn.execute(query)
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()


# UPDATE #################################################################################


@ app.route('/api/employee/update', methods=['PUT'])
# 3) # e)  /api/employee/update
def update_task():
    if not request.json or not 'First Name' and 'Last Name' in request.json:
        abort(400)
    if not request.json:
        abort(400)
    new_person = {
        "First Name": request.json['First Name'],
        "Last Name": request.json['Last Name'],
        "Gender": request.json['Gender'],
        "Age": request.json['Age'],
        "Email": request.json['Email'],
        "Phone": request.json['Phone'],
        "Occupation": request.json['Occupation'],
        "Salary": request.json['Salary']
    }
    editDB(new_person)
    return jsonify({"User was updated to": new_person})


def editDB(update_person):
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@db/db'
    engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
    conn = engine.connect()
    trans = conn.begin()
    try:
        conn.execute("UPDATE Week8People SET Gender='{}', Age='{}', Email='{}', Phone='{}', Occupation='{}', Salary='{}' WHERE `First Name`='{}' AND `Last Name`='{}'".format(
            update_person['Gender'], update_person['Age'], update_person['Email'], update_person['Phone'], update_person['Occupation'], update_person['Salary'], update_person['First Name'], update_person['Last Name']))
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
