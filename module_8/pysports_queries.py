import mysql.connector
from mysql.connector import errorcode

'''
Author: Miguel Juan Lorenzo

This program makes a database connection,
then displays contents for each record in both teams and players tables
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
    #Make connection to database then define mysql statement
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    #Fetch data
    teams = cursor.fetchall()
    #Iterate thorugh each team in teams
    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: ", team[0])
        print("Team Name: ", team[1])
        print("Mascot:", team[2])
        print("")
    #Define mysql statement then iterate through eatch player in playeres
    print("-- DISPLAYING PLAYER RECORDS --")
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
    for player in players:
        print("Player ID: ", player[0])
        print("First Name: ", player[1])
        print("Last Name:", player[2])
        print("Team ID:", player[3])
        print("")
    input("\n\nPress any key to continue...")
#Define exception errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    #Close database connection
    if db is not None:
        db.close()
