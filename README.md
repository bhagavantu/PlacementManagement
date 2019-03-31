Building a placement Management Console Application
Step 1: Project Architecture:
1.There are 8 different attributes of the project. They are: 
		1.	Student Name
		2.	USN Number
		3.	CGPA
		4.	Email.id
		5.	Branch name 
		6.	ID Number (auto generated)
		7.	Password
		8.  Type of Company - Core or IT

2.since we need all of this information to create placement data, we need the following methods:
	1.constructor method for 
      	1.	Student Name
		2.	USN Number
		3.	CGPA
		4.	Email.id
		5.	Branch name 
		6.	ID Number (auto generated)
		7.	Password
	2.Eligibility method to check eligibility of the student for placement
	3.Applied method to find the list of companies applied by the student
	4.Details method to get the full details of the student


Now, we have all the required methods for creating a placement data. But, to ask which type of companies we need to create two child classes from the parent class. Thus, we have two child classes which are:
	1.Core companies
	2.IT companies














