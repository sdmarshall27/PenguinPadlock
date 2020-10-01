import mysql.connector
from Users import Users
from prettytable import PrettyTable
from mysql.connector import Error

u1 = Users()
table = PrettyTable()
table.field_names = ["ID","First Name","Last Name"]
try:
	connection = mysql.connector.connect(user='admin', password='Ysu2020!',
                              host='passwords.c8xiql9k3hrg.us-east-2.rds.amazonaws.com',
                              database='Passwords')
	cursor = connection.cursor()
	cont = True
	while cont:
		userID = int(input("What is the ID of the user you would you like to get information for: "))
		if userID == -1:
			cont = False
		else:
			u1.get_user_info(userID,cursor,Error,table)
except Error as e:
	print("error reading table", e)
finally:
	print("closed")
