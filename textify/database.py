import pymongo
from bson.json_util import dumps




db = None
def setupDatabase():
    global db
    client = pymongo.MongoClient("mongodb+srv://pspiagicw:helloworldtotextify@cluster0.tfus8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['textify-data']
    
def addUserData(id , data):
    collection = db['users-data']
    data_uid = collection.insert_one(data).inserted_id
    return 200

def getUserData(id):
    collection = db['users-data']
    documents = list()
    cursor = collection.find({'uid' : id })
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    print(json_data)
    return 200 , json_data

