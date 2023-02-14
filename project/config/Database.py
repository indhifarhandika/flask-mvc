import mysql.connector

connection = mysql.connector(host="localhost", user="root", password="root")

cursor = connection.cursor()
