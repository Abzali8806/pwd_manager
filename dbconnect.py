import hashlib
import psycopg2
import os


def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
        

def init_db_con(): # rename to user_get_rows
    con = psycopg2.connect(host="172.17.0.1", database="postgres", user="postgres", password="kilk8806")
    cur = con.cursor()
    cur.execute("select * from users;")
    rows = cur.fetchall()

    # commit changes
    con.commit()
    # close cursor
    cur.close
    # close the connection
    con.close()
    return rows


def site_rows():
    con = psycopg2.connect(host="172.17.0.1", database="postgres", user="postgres", password="kilk8806")

    cur = con.cursor()
    cur.execute("select sitename, site_email, password, user_id from site_creds;")
    rows = cur.fetchall() ## used in site_creds_retreive function
    return rows
    
    # commit changes
    con.commit()
    # close cursor
    cur.close
    #close the connection
    con.close()
    