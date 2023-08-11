import mysql.connector
from mysql.connector import errorcode

"""
    Title: whatabook.py
    Author: Miguel Juan Lorenzo
    Date: August 8, 2023
    Description: This application connects to the whatabook database and allows the
    user to interact with it via input/prompts
"""


#Database connection infromation
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    #Commented out becuase I used a different port on my system, leave this uncommented unless you explicitly changed this port
    #"port": 3307,
    "raise_on_warnings": True
}

def show_menu():
    print("-- Main Menu --")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program\n")

    #try/catch block - if input return a ValueError, exit program
    try:
        choice = int(input('Enter an option (1-4): '))
        return choice

    except ValueError:
        print("INVALID ENTRY!\n")
        exit()

def show_books(_cursor):
    #Executes query
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    #Passes query results to books variable
    books = _cursor.fetchall()

    print("\n-- DISPLAYING BOOKS --")

    #Iterate over each element from books variable and outputs book name, author, and details
    for book in books:
        print("Book Name: {}".format(book[0]))
        print("Author: {}".format(book[1]))
        print("Details: {}\n".format(book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

def validate_user():
    #try/catch block for user_id validation
    try:
        user_id = int(input('\nEnter customer id (Example: 1): '))

        #Checks if input is valid
        if user_id < 0 or user_id > 3:
            print("\nUser ID not found, exiting...\n")
            exit()
        return user_id

    except ValueError:
        print("\nInvalid entry, exiting...\n")
        exit()

def show_account_menu():
    #Try/catch block for main menu
    try:
        print("\n-- Customer Menu --")
        print("1. Wishlist")
        print("2. Add Book")
        print("3. Main Menu")
        account_option = int(input('Enter an option (1-3): '))
        return account_option
    #Exits program if it user input returns ValueError, such as entering a string or char
    except ValueError:
        print("\nInvalid entry, exiting...")
        exit()

def show_wishlist(_cursor, _user_id):
    #SQL query for inner join
    _cursor.execute('SELECT user.user_id as "User ID", user.first_name as "First Name", user.last_name as "Last Name", book.book_id as "Book ID", book.book_name as "Book Name", book.author as "Author" FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = 1'.format(_user_id))

    #Passes query results to wishlist variable
    wishlist = _cursor.fetchall()


    print("\n-- DISPLAYING WISHLIST ITEMS FOR USER --")

    #Iterate through each element from wishlist
    for book in wishlist:
        print("Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):

    #Query to display books that are not in specified user's wishlist'
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    #Executes query
    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n-- DISPLAYING AVAILABLE BOOKS --")

    #Iterate through each element in books_to_add
    for book in books_to_add:
        print("Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):

    #Executes INSERT SQL statement
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#try/catch block to call functions and for error handling
try:
    db = mysql.connector.connect(**config) # connect to database

    cursor = db.cursor() # cursor for MySQL queries

    print("\nWhatABook Application")

    user_selection = show_menu()

    #While loop for main menu user selection
    while user_selection != 4:

        #When user_selection is 1, call show_books() function and pass cursor parameter
        if user_selection == 1:
            show_books(cursor)

        #When user_selection is 2, call show_locations() function and pass cursor parameter
        if user_selection == 2:
            show_locations(cursor)

        #When user_selection is 3, call validate_user() function, then call account_option() function
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users
                # configured wishlist items
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    #Prompt user to enter book_id that will be added to wishlist table
                    book_id = int(input("\nEnter Book ID to add to Wishlist: "))

                    #Add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #Commit chage to database
                    db.commit()

                    print("\nBook id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu
                account_option = show_account_menu()

        #When user selection is not 1-4, output Invalid option, try again!, then loops until option is valid
        if user_selection < 1 or user_selection > 4:
            print("\nInvalid option, try again!\n")

        #Call show_menu function
        user_selection = show_menu()

    print("Exiting...")

except mysql.connector.Error as err:

    #Error handling for db connection; outputs message
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    if db is not None:
        #Close connection to db
        db.close()
