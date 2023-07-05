import pymongo

if __name__== "__main__":
    print("This is the output of the following code:")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['test2']
    collection = db['coll2']
    
# Finding a single data    
    # one = collection.find_one({'name':'huzi'})
    # print(one)
        
# Finding multiple data at once
    # allDocs = collection.find({'name':'Huzi'})
    # for item in allDocs:
    #     print(item)
    
    # Printing only required attributes
    allDocs = collection.find({'name':'Huzi'}, {'name': 0, '_id': 0})
    for item in allDocs:
        print(item)
