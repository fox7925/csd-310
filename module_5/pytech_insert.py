from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2yzlobg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
col = db.students
print("-- INSERT STATEMENTS --")
elliot = {
    "first_name": "Elliot",
    "last_name": "Alderson",
    "student_id": "1007"
}
elliot_student_id = col.insert_one(elliot).inserted_id
print(f"Inserted student record {elliot['first_name']} {elliot['last_name']} into the students collection with document_id {elliot_student_id}")

philip = {
    "first_name": "Philip",
    "last_name": "Price",
    "student_id": "1008"
}
philip_student_id = col.insert_one(philip).inserted_id
print(f"Inserted student record {philip['first_name']} {philip['last_name']} into the students collection with document_id {philip_student_id}")

tyrell = {
    "first_name": "Tyrell",
    "last_name": "Wellick",
    "student_id": "1009"
}
tyrell_student_id = col.insert_one(tyrell).inserted_id
print(f"Inserted student record {tyrell['first_name']} {tyrell['last_name']} into the students collection with document_id {tyrell_student_id}")
print("")
input("End of program, press any key to exit... ")
