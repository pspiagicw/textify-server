import pymongo




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
    cursor = collection.find({'id' : id })
    documents = list(cursor)
    return 200 , documents

