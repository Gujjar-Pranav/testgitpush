from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://Pranav:Dhruvi24@cluster0.sr0ekjw.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db3 = client.test
print(db3)
"""
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""

d2= {"name": "Pranav",
     "surname": "Gujjar",
     "email_id": "pranav1329@gmail.com"
}

mdb1 = client['mongodbsetup_1']
coll2 = mdb1['test1']
coll2.insert_one(d2)
