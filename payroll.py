""" The following program calculates the salary for the week of the employees listed below"""

Name = ['Mary','John','Bob','Mel','Jen','Sue','Ken','Dave','Beth','Ray']  # List the name of employees
ID = ['001','002','003','004','005','006','007','008','009','010'] # List ID of employees
Rate =[15,22,35,43,17,29,40,20,37,16.5] # Pay rate list
Hours = [40,25,4,62,33,45,36,17,37,80] # Total hours worked 
employee = list(zip(ID,Name,Rate,Hours))
for emp in employee:
	print(emp[1] + " worked for " + str(emp[3]) + " hours")
	if emp[3] <= 40:
		pay = (emp[2] * emp[3])
		print(" and Pay amount is " + str(pay))
	else:
		pay = (40 * emp[2]) + ((emp[3] - 40)*(emp[2] + emp[2]/2))
		print("Pay amount is " + str(pay))  
		
    
