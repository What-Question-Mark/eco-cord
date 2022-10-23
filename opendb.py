import json
import asyncio
from pymongo import MongoClient

f = open('config.json')
config = json.load(f)

auth_url = config("mongodb-url")

def open_account(id):
    cluster = MongoClient(auth_url)
    db = cluster[config("cluster")]

    cursor = db[config("database")]

    try:
        post = {"_id": id, "wallet": 1000, "bank": 0} 

        cursor.insert_one(post)

    except:
        pass

def get_bank_data(id):
    cluster = MongoClient(auth_url)
    db = cluster[config("cluster")]

    cursor = db[config("database")]

    user_data = cursor.find({"_id": id})

    cols = ["wallet", "bank"] 

    data = []

    for mode in user_data:
        for col in cols:
            data1 = mode[str(col)]

            data.append(data1)

    return data