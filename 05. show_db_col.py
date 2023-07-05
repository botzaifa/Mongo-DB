import pymongo

if __name__== "__main__":
    print("This is the output of the following code:")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['test2']
    collection = db['coll2']
    
# Printing all the DataBases
    allDB = client.list_database_names()
    print(allDB)
    
# Printing all the collections inside the databases
    allCOL = client["test2"]
    print(allCOL.list_collection_names())