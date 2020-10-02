import mysql.connector
from Users import Users
from prettytable import PrettyTable
from mysql.connector import Error

#print("Happy ? to ?",("Birthday","You"))

u1 = Users()
table = PrettyTable()
table.field_names = ["Description","Password"]
try:
	connection = mysql.connector.connect(user='admin', password='Ysu2020!',
                              host='passwords.c8xiql9k3hrg.us-east-2.rds.amazonaws.com',
                              database='Passwords')
	cursor = connection.cursor()
	cont = True
	while cont:
		Email = input("Email: ")
		Password = input("Password: ")
		id = u1.user_login(Email,Password,cursor) 
		if(id> 0):
			print(u1.get_user_info(id,cursor, Error, table))
			break
	print("Succes Login")
except Error as e:
	print("error reading table", e)
finally:
	print("closed")
