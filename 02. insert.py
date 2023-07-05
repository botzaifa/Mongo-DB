import pymongo

if __name__== "__main__":
    print("This is the output of the following code:")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['test2']
    collection = db['coll2']

# Inserion of single data
    # dictionary = {'name':'Huzi', 'age': 20}
    # collection.insert_one(dictionary)
    
    # dict2 = {'name':"huzi", 'college':'TCET'}
    # collection.insert_one(dict2)
    
    # Can have custom 'id' this way:
    # dict3 = {'_id':'1','name':"Huzi","location":'Mumbai'}
    # collection.insert_one(dict3)
    
# Insetion of many data at once    
    # insertThese = [
    #     {'name':'x1', 'location':'Mumbai','marks':20},
    #     {'name':'x2', 'location':'Delhi','marks':18},
    #     {'name':'x3', 'location':'Banglore','marks':19},
    #     {'name':'x4', 'location':'Chennai','marks':12}
    # ]
    # collection.insert_many(insertThese)
    
    insertThese = [
        {'name':'x5', 'location':'Mumbai','marks':20},
        {'name':'x6', 'location':'Delhi','marks':18},
        {'name':'x7', 'location':'Banglore','marks':19},
        {'name':'x8', 'location':'Chennai','marks':12}]
    collection.insert_many(insertThese)