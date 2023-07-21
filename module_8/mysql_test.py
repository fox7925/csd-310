import mysql.connector
from mysql.connector import errorcode

#Test code from cybr-410
#Miguel Juan Lorenzo

#Config dictionary used for specifying database connection
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#Empty db variable
db = None

#Define db variable then print from config dictionary
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\nPress any key to continue...")

#Captures errors and prints output
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

#Close db connection
finally:
    if db is not None:
        db.close()
