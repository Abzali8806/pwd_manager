import psycopg2
import pyperclip
import webbrowser
import time
from dbconnect import init_db_con, clear, site_rows


rows = init_db_con()

def newuser(firstname, lastname, username, masterpwd):
    con = psycopg2.connect(host="172.17.0.1", database="postgres", user="postgres", password="kilk8806")
    curs = con.cursor()
    istrue = False
    while istrue != True:
        if len(masterpwd) < 8:
            print("\n----- Error! -----\n")
            print("master password must be min 8 characters")
            masterpwd = input("enter pwd: ")
            time.sleep(1)
        else:
            curs.execute("insert into users(firstname, lastname, username, master_pwd) values (%s, %s, %s, %s)",(firstname, lastname, username, masterpwd))
            istrue = True

    # commit changes
    con.commit()
    # close cursor
    curs.close
    # close the connection
    con.close()


def account_verify(username, masterpwd):    
    global rows
    # does account exist?
    # ismatch_list = []
    ismatch = False
    # if rows != "[]":
    for r in rows:
        if username == r[3] and masterpwd == r[4]:
            ismatch = True
            return ismatch, r[1]
            break
        else:
            ismatch = False
            return ismatch



# functions: site_creds table data
def add_site_creds(user_id, sitename, site_email, password):
    con = psycopg2.connect(host="172.17.0.1", database="postgres", user="postgres", password="kilk8806")
    cur = con.cursor()
    cur.execute("insert into site_creds(sitename, site_email, password, user_id) values (%s, %s, %s, %s)", (sitename, site_email, password, user_id))
    print("... entry added")
    con.commit()


def retreive_site_creds(user_id, sitename, site_email):
    # Data search-bar
    rows = site_rows()
    ismatch = False
    for r in rows:
        if r[3] == user_id:  # ensure retrieved data correlates with id of logged in user
            if  sitename == r[0] and site_email == r[1]: # ensures correct site entry is examed
                # return r[0], r[1], r[2]
                #ismatch = True #
                creds_2_clipboard(r[0], r[1], r[2])
                break
            else:
                from pwd_manager import start_func
                print("\nrecord not found \nadd site credentials")
                start_func()
                break
        else:
            break

def creds_2_clipboard(sitename,email, password):
    if ".com" in sitename:
        pyperclip.copy()
        print("password copied to clipboard")
    else:
        pyperclip.copy(password)
        print("password copied to clipboard")
        time.sleep(1)
        url = f"{sitename}.com"
        webbrowser.open_new_tab(url)


def list_my_sitecreds(user_id):
    rows = site_rows()
    
    for r in rows:
        if user_id == r[3]:
            print(r)