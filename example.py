import json
import asyncio
from pymongo import MongoClient
from opendb import open_account, get_bank_data
from updatedb import update_bank

# Open Account
open_account()

# Get data
get_bank_data()

# Update data
update_bank()