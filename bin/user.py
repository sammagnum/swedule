#! /Users/smangum/swedule/venv/bin/python3
import getpass
from passlib.hash import argon2
import pymysql.cursors

print("Email:")
username = input()
print("First Name:")
firstname = input()
print("Last Name:")
lastname = input()
h = argon2.using(rounds=11).hash(getpass.unix_getpass())

connection = pymysql.connect(host='127.0.0.1',
                             user='smangum',
                             password='t25ew36z',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "DELETE FROM `user` WHERE `email`=%s"
        cursor.execute(sql,username)
    connection.commit()

    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `user` (`firstname`,`lastname`,`email`, `password`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (firstname, lastname, username, h))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `firstname`, `lastname` FROM `user` WHERE `email`=%s"
        cursor.execute(sql, username)
        result = cursor.fetchone()
        print(result["firstname"] + " " + result["lastname"] + " was sucessfully added.")
finally:
    connection.close()