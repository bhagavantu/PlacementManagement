**Building a placement Management Console Application**
==

**Project Architecture:**

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



# Documentation:
1. To run this project, clone or download this project on your computer.
2. After downoloading the project, open the python3 software if you installed already, otherwise download python 3 software and install    on your computer.
3. Open command prompt, Navigate to the project folder to run this project. For example: folder name is PlacementManagement and in this    folder you have sources file so to open this file use command as mentioned below:

  	      $ cd PlacementManagement/sources
4. After navigation of project folder path, click on program files and open the files on your workspace and save it.
5. To run this project, Run main.py to execute the program using command as mentioned below:

	      $ python main.py
6. After executing the program you can follow the instructions as displayed on your computer and while executing the program you need to    enter valid details then only you can get the correct output
