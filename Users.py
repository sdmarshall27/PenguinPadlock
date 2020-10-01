class Users:
	def __init__(self, ID=0, First_Name="", Last_Name=""):
		self.ID = ID
		self.First_Name = First_Name
		self.Last_Name = Last_Name

	def set_first_name(self, name):
		self.First_Name = name

	def print_User(self):
		print("ID: ",self.ID)
		print("First_Name: ",self.First_Name)

	def get_user_info(self, id, cursor, Error,table):
		select_query= "Select * from Users where ID="+str(id)
		cursor.execute(select_query)
		records = cursor.fetchall()
		if(len(records)>0):
			table.add_row([records[0][0],records[0][1],records[0][2]])
			print (table)
			table.clear_rows()
		else:
			print("No Records Found")
