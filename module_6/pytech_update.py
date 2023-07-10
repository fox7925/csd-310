"""
Author: Miguel Juan Lorenzo

This program displays all documents, updates the record for one student,
and then displays the updated record
"""

from pymongo import MongoClient

#defines connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.2yzlobg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
col = db.students
docs = col.find({})

#call find() and display all documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    student_id = doc["student_id"]
    first_name = doc["first_name"]
    last_name = doc["last_name"]
    print("Student ID:", student_id)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("")

#call update_one() for student_id=1007 and update last_name to "Alders"
col.update_one(
    {"student_id": "1007"},
    {"$set": {"last_name": "Alders"}}
)

#call find_one() for student_id=1007 and display document
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
doc = col.find_one({'student_id': '1007'})
student_id = doc["student_id"]
first_name = doc["first_name"]
last_name = doc["last_name"]
print("Student ID:", student_id)
print("First Name:", first_name)
print("Last Name:", last_name)
print("")
print("")
input("End of program, press any key to exit... ")
