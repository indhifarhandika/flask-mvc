import mysql.connector

connection = mysql.connector(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = connection.cursor()
