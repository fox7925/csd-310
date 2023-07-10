"""
Author: Miguel Juan Lorenzo

This program inserts a new record, then deletes it in the following order
1. Display all documents
2. Insert new document
3. Display newly created document
4. Delete newly created document
5. Displays all documents again
"""

from pymongo import MongoClient

# defines connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.2yzlobg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
col = db.students
docs = col.find({})

# call find() and display all documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    student_id = doc["student_id"]
    first_name = doc["first_name"]
    last_name = doc["last_name"]
    print("Student ID:", student_id)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("")

# call insert_one() and insert a new document for student_id=1010
terry = {
    "first_name": "Terry",
    "last_name": "Colby",
    "student_id": "1010"
}
terry_student_id = col.insert_one(terry).inserted_id
print("-- INSERT STATEMENTS --")
print(
    f"Inserted student record {terry['first_name']} {terry['last_name']} into the students collection with document_id {terry_student_id}")
print("")

# call find_one() for student_id=1010 and display results
print("-- DISPLAYING STUDENT TEST DOC --")
doc = col.find_one({'student_id': '1010'})
student_id = doc["student_id"]
first_name = doc["first_name"]
last_name = doc["last_name"]
print("Student ID:", student_id)
print("First Name:", first_name)
print("Last Name:", last_name)
print("")

# call delete_one() for student_id=1010
col.delete_one({'student_id': '1010'})

#redfine col.find() variable
docs = col.find({})

# call find() and display all documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    student_id = doc["student_id"]
    first_name = doc["first_name"]
    last_name = doc["last_name"]
    print("Student ID:", student_id)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("")
print("")
input("End of program, press any key to continue...")
