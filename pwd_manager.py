import psycopg2
import time
import hashlib
from dbconnect import clear, init_db_con
from backend import newuser, account_verify, add_site_creds, list_my_sitecreds, retreive_site_creds


# connect to db
init_db_con()
usertbl_rows = init_db_con()

def signup_creds():
    print("---------- sign up ----------\n")
    firstname = input("enter name: ")
    lastname = input("enter lastname: ")
    print("master password: minimum 8 characters")
    masterpwd = input("enter master passwords: ")
    print(f"\n your new username is {firstname}.{lastname}")
    time.sleep(3)
    print("\n\n ...loading")
    return firstname, lastname, masterpwd


def u_id(username, masterpwd):  # move to backend.py
    con = psycopg2.connect(host="172.17.0.1", database="postgres", user="postgres", password="kilk8806")
            ## execute query / pull dat
    cur = con.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    for r in rows:
        if username != r[3] and masterpwd != r[4]:
            None
        else:
            return r[0]
    
    # commit changes
    con.commit()
    # close cursor
    cur.close
    # close the connection
    con.close()

# programs starts here:
def start_func():
    print("Login/Sign up")
    start_query = input(">: ")
    time.sleep(1)
    return start_query
    clear()

start_query = start_func()

if start_query.lower() == "sign up" or start_query.lower() == "signup":
    creds = signup_creds()
    firstname = creds[0]
    lastname = creds[1]
    username = firstname+"."+lastname
    masterpwd = creds[2]

    newuser(firstname, lastname, username, masterpwd)

    time.sleep(1)
    user_id = u_id(username, masterpwd)


if start_query.lower() == "login":
    print("---------- Login----------\n")
    print("enter your username & master password\n")
    # enter login credentials
    print("Username format: firstname.lastname")
    username = input("username: ")
    masterpwd = input("master password: ")
    result = account_verify(username, masterpwd)
    ismatch = result[0]
    # print(ismatch)
    if not ismatch:
        start_func()
    else:
        user_id = u_id(username, masterpwd)
        firstname = result[1]
else:
    pass


# clear()
def main_menu():
    global firstname
    clear()
    print(f"Welcome {firstname}\n")

    print("--------------- MENU ---------------\n")
    print("enter number")
    print("1. add new site credentials \n2. retrieve site credentials \n3. list all your site credentials \nQ. Quit\n")
    num = input("> ")
    return num

choice = main_menu()

def post_choice(choice):
    if choice == "1":
        print("---------- add account credentials apps ----------\n")
        sitename = input("Website: ")
        site_email = input("site email: ")
        password = input("password!!!: ")
        clear()
        add_site_creds(user_id, sitename, site_email, password)
    elif choice == "2":
        print("----------- retreieve site credentials -----------\n")
        sitename = input("Website: ")
        site_email = input("site email: ")
        # data_rows= 
        retreive_site_creds(user_id, sitename, site_email)
        # print(data_rows)
    elif choice == "3":
        clear()
        list_my_sitecreds(user_id)
        time.sleep(3)
        # print(mysites)
    elif choice.upper() == "Q":
        print("Goodbye")
        exit()

post_choice(choice)

def follow_up():
    print("Do you want to continue? y/n")
    reply = input("> ")
    while reply.lower() == "y" or "yes":
        choice = main_menu()
        post_choice(choice)
    else:
        exit()

follow_up()
