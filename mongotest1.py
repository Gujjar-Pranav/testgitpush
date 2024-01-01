from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Pranav:Dhruvi24@cluster0.sr0ekjw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.test
print(db)

d = {
    "name": "Pranav",
    "surname": "Gujjar",
    "email_id": "pranav1329@gmail.com"}

d4 = {"car": "hyndai", "bike": "yamaha", "plane": "vistara"}

d5 = {"car": "toyota", "bike": "honda", "plane": "airindia"}

mdb = client['mongodbsetup_1']
coll = mdb['test']
coll.insert_one(d)
coll.insert_one(d4)
coll.insert_one(d5)
