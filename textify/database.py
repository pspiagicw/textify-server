import pymongo




db = None
def setupDatabase():
    global db
    client = pymongo.MongoClient("mongodb+srv://pspiagicw:helloworldtotextify@cluster0.tfus8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['textify-data']
    
def Set(id , data):
    collection = db['users-data']
    final_data = dict(user =id , **data)
    data_uid = collection.insert_one(final_data).inserted_id
    return 500

def GetAll(id):
    collection = db['users-data']
    documents = list()
    cursor = collection.find({})
    for i in cursor:
        documents.append(cursor)
    return 500 , documents

