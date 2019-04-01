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