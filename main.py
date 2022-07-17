import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.ttims.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"shubham",
    "email": "shuabhasnfbafv@gmail.com",
    "surname" : "madihalli"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )