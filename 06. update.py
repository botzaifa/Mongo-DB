import pymongo

if __name__== "__main__":
    print("This is the output of the following code:")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['test2']
    collection = db['coll2']
    
    PKey = {"name":"x4"}
    noww = {"$set": {"location":"Kashmir"}}
    collection.update_one(PKey , noww)