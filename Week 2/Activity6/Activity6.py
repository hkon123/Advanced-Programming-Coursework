import pymongo
import json

def dbSetup(client):

    db = client["University"]
    collection = db["studentAdmin"]
    with open("People.json") as file:
        data = json.load(file)
        for item in data.get("students"):
            ins = collection.insert_one(item)

def getNameOver25(collection):

    print("People with age over 25:")
    results = collection.find({'age':{'$gt':25}}, {'_id':0,'fullName':1})
    for r in results:
        print(r)
    return results

def getNoMidlleName(collection):

    print("People with with no middle name:")
    results = collection.find({'fullName.other':{'$eq':[None]}}, {'_id':0, 'id':1})
    for r in results:
        print(r)
    return results

def getNumNotInTokyo(collection):

    resultsMen = collection.find({'city':{'$ne':'Tokyo'}, 'fullName.title':{'$eq':'Mr'}}, {'_id':0, 'id':1})
    resultsWomen = collection.find({'city':{'$ne':'Tokyo'}, 'fullName.title':{'$ne':'Mr'}}, {'_id':0, 'id':1})
    print(f"{len(list(resultsMen))} men, and {len(list(resultsWomen))} women do not live in Tokyo")

def exercise1():

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    if ("University" in client.list_database_names()) == False:
        dbSetup(client)

    collection = client["University"]["studentAdmin"]
    getNameOver25(collection)
    getNoMidlleName(collection)
    getNumNotInTokyo(collection)

def main():

    exercise1()

if __name__ == "__main__":
    main()
