import mysql.connector.connection

connection = mysql.connector.connection.MySQLConnection(
    host="localhost", user="root", password="root"
)

cursor = connection.cursor()
