class Users:
	def __init__(self, UserID=0, FirstName="", LastName="", Email="", Password=""):
		self.UserID = UserID
		self.FirstName = FirstName
		self.LastName = LastName
		self.Email = Email
		self.Password = Password

	def set_first_name(self, name):
		self.First_Name = name

	def print_User(self):
		print("ID: ",self.ID)
		print("First_Name: ",self.First_Name)

	def get_user_info(self, id, cursor, Error,table):
		select_query= "Select * from Password where OwnerID="+str(id)
		cursor.execute(select_query)
		records = cursor.fetchall()
		if(len(records)>0):
			for record in records:
				table.add_row([record[1],record[2]])
			print (table)
			table.clear_rows()
		else:
			print("No Records Found")

	def user_login(self,email,password,cursor):
		select_query = "Select * from User where Email = '"+email+"' && Password = SHA1('"+password+"')"
		print(select_query)
		cursor.execute(select_query)
		records = cursor.fetchall()
		if(len(records)>0):
			print("Login Success")
			return records[0][0]
		else:
			return -1
