**Building a placement Management Console Application**
==

**Step 1: Project Architecture:**

1. There are 8 different attributes of the project. They are:
	* Student Name
	* USN Number	
	* CGPA
	* Email.id
	* Branch name 
	* ID Number (auto generated)
	* Password
	* Type of Company - Core or IT

2. since we need all of this information to create placement data, we need the following methods:
	1. constructor method for:  
		* Student Name
		* USN Number
		* CGPA
		* Email.id
		* Branch name 
		* ID Number (auto generated)
		* Password  
	2. Eligibility method to check eligibility of the student for placement
	3. Applied method to find the list of companies applied by the student
	4. Details method to get the full details of the student

Now, we have all the required methods for creating a placement data. But, to ask which type of companies we need to create two child classes from the parent class. Thus, we have two child classes which are:

	1. Core companies
	2. IT companies
# Flow chart
![WhatsApp Image 2019-04-01 at 9 07 20 PM](https://user-images.githubusercontent.com/49069957/55340473-66682280-54c2-11e9-8c85-44c9925f2d8f.jpeg)

*This is the flowchart that I had created for the application that I was building. I hope this flowchart is self-explanatory. If you have any doubts feel free to ping me.
Below, based on this flowchart I’ve written the boilerplate code for the application. I also want you to do the same for your application.*

# Boilerplate code for Complete Project
# placement.py 
```python
IT_companies={"Accenture":6.7, "Mindtree":7, "Apple":8.5, "Infosis":8}
core_companies={"Bosch":7.2, "Sankalp":8, "Siemen":8.5, "Shnieder":7.8}
companies={"Accenture":6.7, "Mindtree":7, "Apple":8.5, "Infosis":8, "Bosch":7.2, "Sankalp":8, "Siemen":8.5, "Schnieder":7.8}
class PlacementManagement:
	"""
	General Data Class for a place Management
	"""

	def __init__(self, name, usn,cgpa, email, branch, id_number, password):
		"""
		Constructor function for the Data Class
		Executed by interpreter to create an instance of this class.
		Attributes:
			self.name -- name of the student (str)
			self.usn -- usn of student  
			self.cgpa -- cgpa of the student (float)
			self.email --  email id of student
			self.branch -- branch of student (str)
			self.id_no -- id number to create the placement data (int)
			self.password -- password to access the account
		"""
		self.name = name
		self.usn = usn
		self.cgpa = (cgpa)
		self.email = email
		self.branch = branch
		self.id_number = id_number
		self.password= password 	

	def eligibility(self):
		# To check the elibility of student for the placement

		if self.cgpa > 6.5:
			print("Eligible for the placement")
				
		else:
			print("Sorry! not eligible for placement")

	def applied(self):
		
		# To find the various of companies applied by the student
		print(companies) 
		
		for company, comp_cgpa in companies.items():
			#It compares the student cgpa with company cgpa
			if self.cgpa >= comp_cgpa:
				print("applied company name is:",company)
				
				
		else:
				print("You not applied for this company:", company)


	def details(self):
		# To get the  student full details
		print("\n\ncandidate details:")

		print("\t\tname:", self.name)
		print("\t\tusn:", self.usn)
		print("\t\temail:", self.email)
		print("\t\tcgpa:", self.cgpa)
		print("\t\tbranch:", self.branch,"\n\n")

		
		

	


	#-----------------------------------
	#child class1
class CoreCompanies(PlacementManagement):


	def eligibility(self):
		# To check the elibility of student for the placement
		
		if self.cgpa < 7.0:
			print(" sorry! minimum cgpa will be 7.0 ")
		else:
			print(" Hey! Congrats you are Eligible for the placement\nSelect 3 to Apply for company\n")

	def applied(self):
		# To find the various of companies available for the student
		if self.cgpa>7.0:
			print("\nHey! you can see here list of  core companies and its cut off cgpa for job application:\n")
		
		for key, value in core_companies.items():
			#It compares the student cgpa with company cgpa
			if self.cgpa >= value:
				print("company name is",key,"Required cgpa is",value)
		if self.cgpa<7.0:	
			print("\nsorry! companies are not available because you have less cgpa")
		else:
			company_name=input("\nif you wants to apply for job enter the  campany name from the list of  core companies as mentioned above :\n")
			if company_name in core_companies.keys():
				print("\nYou successfully applied for ",company_name)
				print("\nThank you for choosing CoreCompanies\n ")
			else:
				print("\nSorry! what  you entered company name is not available: ")




class ITCompanies(PlacementManagement):

	def eligibility(self):
		
		if self.cgpa < 6.5:
			print(" sorry! minimum cgpa will be 6.5 ")
		else:
			print("Congrats you are Eligible for the placement\nSelect 3 to Apply for company\n")

	def applied(self):
		# To find the various of companies available for the student
		if self.cgpa>6.5:
			print("Hey! you can see here list of  core companies and Required cgpa for job application:\n")


		for key, value in IT_companies.items():
			#It compares the student cgpa with company cgpa
			if self.cgpa >= value:
				print("company name is",key,"Required cgpa is",value)	
		if self.cgpa<6.5:	
			print("\nsorry! companies are not available because you have less cgpa")
		else:
			company_name=input("\nif you wants to apply for job enter the  campany name from the list of  core companies as mentioned above :\n")
			if company_name in IT_companies.keys():
				print("\nYou successfully applied for ",company_name)
				print("\nThank you for choosing ITCompanies\n ")
			else:
				print("\nSorry! what  you entered company name is not available:")
``` 

# main.py
```python
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
id_number = 100
print(" Welcome to placement management")
# Application Loop

while True:
	print("\n\nHey! What would you like to do today?\n\n\
		1. Create Placement Data\n\
		2. Check Eligibility\n\
		3. Apply for a Company\n\
		4. Candidate full details\n\
		5. Exit\n")
	try:
		choice = int(input("Enter your option: "))
	except:
		print("\n\nPlease Select Correct Option")
		continue
	if choice == 1:
		"""If user choice is 1  – Create new placement data with info """

		# Ask for basic info needed to create a data
		name = input("Enter your name: ")
		usn = input("Enter your usn: ")
		cgpa = input("Enter your cgpa: ")
		email =input("Enter your email: ")
		branch = input("Enter your department: ")
		password =input("Enter your password: ")
		try:
			cgpa=float(cgpa)
		except:
			print("\n\nPlease enter cgpa in number\nPlease enter the Details Again ")
			continue

		if name.isnumeric()==True or branch.isnumeric()==True:
			print("\n\nInvalid Details\nPlease Enter Correct Details\n")
			continue

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
		try:
			choice=int(input("Enter the type of   companies you want?\n 1.CoreCompanies \n 2.ITCompanies \n"))
		except:
			print("invalid choice")
			continue

		# To check the elibility of student for the placement
		if choice==1:
			try:
				if (upassword == core_data[id_no].password):
					core_data[id_no].eligibility()

				else:
					print("\nInvalid password. Please enter again!\n\n")
			except:
				print("\nInvalid placement id number.Please enter again!\n ")
			
				

		elif choice==2:
			try:
				if (upassword == IT_data[id_no].password):
					IT_data[id_no].eligibility()
			
				else:
					print("\nInvalid  password. Please enter again!\n\n")
			except:
				print("\nInvalid placement id number.\nPlease enter again!\n ")

		else:
			print("\nPlease! choose correct option")

			
	elif choice ==3:
		""" 
		If user choice is 3  – perform process of  student applied for the placement
		"""
		# Get User Account Details
		id_no =eval(input("Enter your placement ID number "))
		upassword = input("Enter the password: ")
		try:
			choice=int(input("Enter the type of   companies you want?\n 1.CoreCompanies \n 2.ITCompanies \n"))
		except:
			print("invalid choice")
			continue

		if choice==1:
			try:
				if upassword == core_data[id_no].password:
					core_data[id_no].applied()
					

				else:
					print("\n\nInvalid  password . Please enter again!\n\n")
			except:
				print("\nInvalid placement id number.Please enter again!\n ")


		elif choice==2:
			try:
				if upassword == IT_data[id_no].password:
					IT_data[id_no].applied()
					
				else:
					print("\nInvalid password Details. Please enter again!\n\n")
			except:
				print("\nInvalid placement id number.Please enter again!\n ")

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
		try:
			if upassword == students_data[id_no].password:
				students_data[id_no].details()
			else:
				print("\nInvalid password. plese enter again!\n")
		except:
				print("\nInvalid placement id number.Please enter again!\n ")
			
	elif choice ==5:
		print("\nThank You\n")
		break
	else: 
		print("\nPlease! choose correct option")




```
