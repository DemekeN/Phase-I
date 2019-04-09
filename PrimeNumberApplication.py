""" The following application show a list of numbers and indicate whether or not they are prime.
This application lets user to input the last number in the range, and print all of the numbers from 2 to that number.
"""
number = int(input("Enter the last number"))
primes = []
for number in range(2,number+1):
	prime = True
	for i in primes:
		if not (number % i):
			print(number, ' is not a prime')
			prime = False
			break
	if prime == True:
		print(number, ' is a prime')
		primes.append(number)
