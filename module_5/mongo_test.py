from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2yzlobg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech COllection List --")
print(db.list_collection_names())
print("")
input("End of program, press any key to exit... ")
