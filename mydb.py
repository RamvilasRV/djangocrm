import mysql.connector

dataBase = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "root"
	)

# prepare cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database connection setup")