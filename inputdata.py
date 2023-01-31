import requests
from pymongo import MongoClient

# Client connects to "localhost" by default
client = MongoClient()

# Create local "nobel" database on the fly
db = client["nobel"]

for collection_name in ["prizes", "laureates"]:
# collect the data from the API
    response = requests.get("http://api.nobelprize.org/v1/{}.json".\
        format(collection_name[:-1] ))

    # convert the data to json
    documents = response.json()[collection_name]

    # Create collections on the fly
    db[collection_name].insert_many(documents)
