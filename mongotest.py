import pymongo

const { MongoClient } = require('mongodb');
const uri = "mongodb+srv://shubham:shubham123@cluster0.ttims.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});

db = client.test
print(db)afnsdjklfgjksd