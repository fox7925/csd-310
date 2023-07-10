from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.2yzlobg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
col = db.students
docs = col.find({})

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

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = col.find_one({'student_id': '1007'})
student_id = doc["student_id"]
first_name = doc["first_name"]
last_name = doc["last_name"]
print("Student ID:", student_id)
print("First Name:", first_name)
print("Last Name:", last_name)
print("")
input("End of program, press any key to exit... ")
