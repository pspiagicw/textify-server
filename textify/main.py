from flask import Flask , jsonify , request , Response
from uuid import uuid1
import time
from textify import database

app = Flask(__name__)
database.setupDatabase()

@app.route('/login')
def newlogin():
    data = {
        'id': uuid1(),
        'timestamp': time.time()
    }
    return jsonify(data)

@app.route('/pull/<id>' , methods=['GET'])
def getdata(id):
    status , data = database.getUserData(id)
    return jsonify(data) , status

@app.route('/push/<id>' , methods=['POST'])
def setdata(id):
    data = request.get_json()
    final_data = dict(uid = id , **data)
    response = database.addUserData(id , final_data)
    return Response(status = response)

    
if __name__ == '__main__':
    app.run(debug=True)
