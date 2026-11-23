from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://suvarna7salunkhe_db_user:9WZjm4vjc4SM2-2@cluster0.nuuozzj.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)