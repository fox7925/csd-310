import mysql.connector
from mysql.connector import errorcode

'''
Author: Miguel Juan Lorenzo

This program connects to mariadb, then runs 6 sql queries in the following order:
INSERT new record
SELECT all from inner join
UPDATE newly created record
SELECT all from inner join
DELETE newly created record
SELECT all from inner join
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
db = mysql.connector.connect(**config)
cursor = db.cursor()

#SQL queries
query_insert = "INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (21, 'Smeagol', 'Shire Folk', 1)"
query_update = "UPDATE player SET team_id = 2 WHERE player_id = 21 AND first_name = 'Smeagol' AND last_name = 'Shire Folk' AND team_id = 1"
query_delete = "DELETE FROM player WHERE player_id = 21 AND first_name = 'Smeagol' AND last_name = 'Shire Folk' AND team_id = 2"
query_select = "SELECT p.player_id, p.first_name, p.last_name, t.team_name FROM player AS p INNER JOIN team AS t ON p.team_id = t.team_id"

try:
    # Execute and commit query_insert
    cursor.execute(query_insert)
    db.commit()
    # Execute, commit, and output query_select
    cursor.execute(query_select)
    players = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    for player in players:
        print("Player ID: ", player[0])
        print("First Name: ", player[1])
        print("Last Name:", player[2])
        print("Team Name:", player[3])
        print("")

    # Execute and commit query_update
    cursor.execute(query_update)
    db.commit()
    # Execute, commit, and output query_select
    cursor.execute(query_select)
    players = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    for player in players:
        print("Player ID: ", player[0])
        print("First Name: ", player[1])
        print("Last Name:", player[2])
        print("Team Name:", player[3])
        print("")

    # Execute and commit query_delete
    cursor.execute(query_delete)
    db.commit()
    # Execute, commit, and output query_select
    cursor.execute(query_select)
    players = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER DELETE --")
    for player in players:
        print("Player ID: ", player[0])
        print("First Name: ", player[1])
        print("Last Name:", player[2])
        print("Team Name:", player[3])
        print("")

    input("Press any key to continue...")

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
