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
 










