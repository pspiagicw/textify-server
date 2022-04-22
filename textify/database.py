import pymongo




db = None
def setupDatabase():
    global db
    client = pymongo.MongoClient("mongodb+srv://pspiagicw:helloworldtotextify@cluster0.tfus8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['textify-data']
    
def addUserData(id , data):
    collection = db['users-data']
    final_data = dict(uid =id , **data)
    data_uid = collection.insert_one(final_data).inserted_id
    return 500

def getUserData(id):
    collection = db['users-data']
    documents = list()
    cursor = collection.find({'uid' : id })
    for i in cursor:
        documents.append(cursor)
    return 500 , documents

