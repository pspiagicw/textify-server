from flask import Flask , jsonify , request , Response
from uuid import uuid1
import time
from textify import database

app = Flask(__name__)
database.setupDatabase()

@app.route('/new')
def newlogin():
    data = {
        'id': uuid1(),
        'timestamp': time.time()
    }
    return jsonify(data)

@app.route('/get/<id>' , methods=['GET'])
def getdata(id):
    status , data = database.GetAll(id)
    return jsonify(data) , status

@app.route('/set/<id>' , methods=['POST'])
def setdata(id):
    data = request.get_json()
    print(data)
    response = database.Set(id , data)
    return Response(status = response)

    
if __name__ == '__main__':
    app.run(debug=True)
