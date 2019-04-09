""" 
Write a program that prints the numbers from 1 to 100.

For multiples of 3 print “Fizz” instead of the number.

For the multiples of five print “Buzz”.

For numbers which are multiples of both 3 and 5 print “FizzBuzz”.
"""

for x in range(1,100):
    if (x%5== 0) & (x%3==0):
        print('FIZZBUZZ')
    elif x%3 == 0:
        print('FIZZ')
    elif x%5 ==0:
        print('BUZZ')
    else:
        print(x)