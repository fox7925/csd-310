import mysql.connector
from mysql.connector import errorcode

'''
Author: Miguel Juan Lorenzo

This program makes a database connection,
then displays contents of join for player and team tables
'''

#Dictionary defining databse information
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = None
try:
    #Make connection to database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    #MySQL join statement
    cursor.execute("select p.player_id, p.first_name, p.last_name, t.team_name from player as p inner join team as t on p.team_id = t.team_id")
    players = cursor.fetchall()
    print("-- DISPLAYING PLAYER RECORDS --")
    #Iterate through each player from mysql statement output
    for player in players:
        print("Player ID: ", player[0])
        print("Team Name: ", player[1])
        print("Last Name:", player[2])
        print("Team Name:", player[3])
        print("")
    input("\n\nPress any key to continue...")
except mysql.connector.Error as err:
    #Catch errors and print error messages
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    #Close database connection when db not equal to None
    if db is not None:
        db.close()
