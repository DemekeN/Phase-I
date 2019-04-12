"""The following program mimics the Magic 8 Ball. Magic ball is a ball containing a clear window,
you shake the ball and ask it a question. A random response rises to the window.
"""

import random

Possible_Answer = ["It is certain","It is decidely so","Without a doubt","Yes definitely","As I see it, yes","Most likely","Concentrate and ask again",
               "Better not tell you now","Yes","My reply is no","My sources say no","It could be so.","I guess so.","Very doubtful."]

def say_answer():
        rand_num = random.randint(0,len(Possible_Answer)-1)
        print(Possible_Answer[rand_num])


More_questions = True

while More_questions:
        print("Magic 8_ball: Ask me question.")
        question = input()
        say_answer()
        yes_no = input("Magic 8_ball :Any more questions for me? (y/n)")
        if str.lower(yes_no) == 'n':
                More_questions = False

print("Magic 8_ball: Thank you for playing come back again")


