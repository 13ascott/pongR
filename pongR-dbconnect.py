""" Script to run the python/Kivy GUI to interact with the local MariaDB database titled "compoundpingpong" """

import mariadb
import sys

def dbconnect:
    try:
        conn = mariadb.connect(user="localuser",password="Welcome1",host="localhost",port=3306,database="compoundpingpong")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)

    cur = conn.cursor()

    cur.execute("SELECT * FROM players")

    for idnum, lastname, firstname, birthdate, profpic in cur:
        print(f"{firstname} {lastname}")

    conn.close()

    return

