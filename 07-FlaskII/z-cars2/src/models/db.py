import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="z_cars2",
)
