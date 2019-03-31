from placement import PlacementManagement,CoreCompanies,ITCompanies
""" 
**Variables** 
Student_data: (dict) {id_number: placement management Object} holds all the accounts created during the session.
core_data: (dict) {id_number: CoreCompanies Object}
IT_data: (dict) {id_number: ITCompanies Object}
id_number: (int) - Set to 0 by default ,id number . allocation starts here. Incremented after every new placement data
creation 
"""
core_data={}
IT_data={}
students_data={}
id_number = 0
print(" Welcome to placement management")
# Application Loop

while True:
	print("\n\nHey! What would you like to do today?\n\n\
		1. Create Placement Data\n\
		2. Check Eligibility\n\
		3. show applied details\n\
		4. candidate full details\n\
		5. Exit\n")
	
	choice = int(input("Enter your option: "))

	if choice == 1:
		"""If user choice is 1  – Create new placement data with info """

		# Ask for basic info needed to create a data
		name = input("Enter your name: ")
		usn = input("Enter your usn: ")
		cgpa = input("Enter your cgpa: ")
		email =input("Enter your email: ")
		branch = input("Enter your department: ")
		password =input("Enter your password: ")

		# Use the current id_number count to assign an id number and save the object as students_data
		students_data[id_number]=PlacementManagement(name, usn,cgpa, email, branch, id_number, password)
		core_data[id_number]=CoreCompanies(name, usn,cgpa, email, branch, id_number, password)
		IT_data[id_number]=ITCompanies(name, usn,cgpa, email, branch, id_number, password)

		
		print(f"\nPlacement Data created successfully! Your  Placement ID number is {id_number}")
		# Increment the count after successful creation of placement data
		id_number =id_number + 1
	

	elif choice ==2:
		""" 
		If user choice is 2  - perform eligibility process 
		"""
		# Get User Account Details
		id_no =int(input("Enter your placement ID number: "))
		upassword = input("Enter the password: ")
		choice=int(input("Enter the type of   companies you want?\n 1.CoreCompanies \n 2.ITCompanies \n"))

		# To check the elibility of student for the placement
		if choice==1:
			
			if upassword == core_data[id_no].password:
				core_data[id_no].eligibility()
				print("\nThank you for choosing CoreCompanies ")

			else:
				print("\nInvalid Placement id and password Details. Please enter again!\n\n")

			
				

		elif choice==2:
			
			if upassword == IT_data[id_no].password:
				IT_data[id_no].eligibility()

				print("\nThank you for choosing ITCompanies ")
			
			else:
				print("\nInvalid Placement id and password Details. Please enter again!\n\n")
		else:
			print("Please! choose correct option")

			
	elif choice ==3:
		""" 
		If user choice is 3  – perform process of  student applied for the placement
		"""
		# Get User Account Details
		id_no =eval(input("Enter your placement ID number "))
		upassword = input("Enter the password: ")
		choice=int(input("Enter the type of  you want?\n 1.CoreCompanies \n 2.ITCompanies \n"))

		if choice==1:
		
			if upassword == core_data[id_no].password:
				core_data[id_no].applied()
				print("Thank you for choosing CoreCompanies ")

			else:
				print("\n\nInvalid  Placement id and password Details. Please enter again!\n\n")


		elif choice==2:
			
			if upassword == IT_data[id_no].password:
				IT_data[id_no].applied()
				print("\nThank you for choosing ITCompanies ")
			else:
				print("\nInvalid Placement id and password Details. Please enter again!\n\n")

		else:
			print("Please! choose correct option")



	elif  choice ==4:
		""" 
		If user choice is 4  – show full details of student
		"""

		# Get User Account Details
		id_no = eval(input("Enter your placement ID number "))
		upassword = input("Enter the password: ")

		# To get the  student full details
		if upassword == students_data[id_no].password:
			students_data[id_no].details()
		else:
			print("\nInvalid details. plese enter again!")
			
	
	else: 
		print("Please! choose correct option")



