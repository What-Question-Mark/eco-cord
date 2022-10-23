import json
import asyncio
from pymongo import MongoClient

f = open('config.json')
config = json.load(f)

auth_url = config("mongodb-url")

def update_bank(id, amount=0, mode="wallet"):
    cluster = MongoClient(auth_url)
    db = cluster[config("cluster")]

    cursor = db[config("database")]

    cursor.update_one({"_id": id}, {"$inc": {str(mode): amount}})