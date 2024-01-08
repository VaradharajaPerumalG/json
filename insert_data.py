import json
from pymongo.mongo_client import MongoClient

db_url = "mongodb+srv://VaradharajaPerumal:<54410>@varadharajaperumal.jlcs4d1.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_url)

print(client)