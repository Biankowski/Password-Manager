# Import necessary Modules.
from re import S
import mysql.connector
from bullet import Password

# Connect to the Database. 
# You need to have an existing Databse to be able to connect.
# If you don't have it, create one using the SQL sintax and change the database name to the one that you created.
mydb = mysql.connector.connect(host="localhost", user="", password="", database="Password_manager")
mycursor = mydb.cursor()

# Function to Insert Data into the Database.
def new_data():
    print("Type the Username and password you want to add to the database:")
    username = input("Username: ") # Here is the Username that will be inserted to the database
    password = input("Password: ") # Here is the password that will be inserted to the database. WARNING - This password will be stored in plain text.

    
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)" # SQL Syntax.
    val = (username, password)

    mycursor.execute(sql, val)

    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)

# Function to Get Data from the Database.
def get_data():

    lista = [] # This variable will store the Username inputed by the user inside a list. This is needed because we need to pass a list to the "mycursor.execute" function
    sql = ("SELECT password FROM users WHERE username = %s") # SQL Syntax.
    get = input("Type the Username you want to get: ")
    lista.append(get) # This will add the username inputed by the user into the "lista" variable
    
    mycursor.execute(sql, lista)

    myresult = mycursor.fetchall()

    print(get)
    print(myresult)

# Function to Delete Data from the Database.
def delete_data():
    loop = True
    while loop == True: # Loop to keep prompting the user to delete multiple users at once, without the need to run the program over and over again.
        lista = [] # This variable will store the Username inputed by the user inside a list. This is needed because we need to pass a list to the "mycursor.execute" function
        sql = ("DELETE FROM users WHERE username = %s") # SQL Syntax
        get = input("Type the Username you want to delete from database: ")
        lista.append(get) # This will add the username inputed by the user into the "lista" variable

        mycursor.execute(sql, lista)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted" )
        print("")
        cont = input("Do you wish to delete another Username from database? " "Y/n ") # continue variable.
        if cont == 'y' or cont == 'Y' or cont == 'Yes' or cont == 'yes' or cont == 'YES':
            loop = True
        elif cont == 'n' or cont == 'N' or cont == 'No' or cont == 'no' or cont == 'NO':
            loop = False
        else:
            print("Something went wrong!")
            loop = False

# Main Username and Password to login into the Password Manager
main_username = ""
main_password = ""

log_in = input("Username: ")
cli = Password(prompt="Password: ", hidden="*") # Use this module to hide password when typing on the terminal.
pass_word = cli.launch()


if log_in == main_username and pass_word == main_password:


# Basic ASCII art - https://fsymbols.com/text-art/
    print("""
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░  ██╗░░░██╗░█████╗░██╗░░░██╗██╗░░░░░████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗  ██║░░░██║██╔══██╗██║░░░██║██║░░░░░╚══██╔══╝
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║  ╚██╗░██╔╝███████║██║░░░██║██║░░░░░░░░██║░░░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║  ░╚████╔╝░██╔══██║██║░░░██║██║░░░░░░░░██║░░░
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝  ░░╚██╔╝░░██║░░██║╚██████╔╝███████╗░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░""")
    print("Welcome to Rodrigo's Password Manager.")

# Option menu
    option = input("""\nPlease select an action you want to do: 
    1) Insert new data in database
    2) Retrieve data from database
    3) Delete data from database
    """)

# Execute functions based on user option
    if option == '1':
        new_data()
    elif option == '2':
        get_data()
    elif option =='3':
        delete_data()
else:
    print("Authentication Falied.")
