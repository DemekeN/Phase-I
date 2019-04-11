""" Eliza is a therapist program that interacts with the user. 
This  program will need to evaluate what the user asks and turn the
user's input into a question that sounds like the therapist really cares.
If the user types in "I am feeling great" or enter "Q", the program will stop running.
The program should print out the last input (as an output) every time before accepting new input
and also accommodates for NO case-sensitivity. (Q is the same as q) """


greeting = " Good day. What is your problem? Enter your response here or Q to quit: "
answer = True
while answer:
    message =input(greeting)
    response = message.lower()
    print("You answered: '" + message + "'")
    if response == 'q' or str.lower(message) ==  'i am feeling great':
        answer = False
print("Thanks, have a great day")
      






