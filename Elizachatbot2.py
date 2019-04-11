"""
 Eliza is a therapist program that interacts with the user.
 The program will need to evaluate what the user asks and turn the user's
 input into a question that sounds like the therapist really cares.

The user enters something at the prompt: "my teacher hates me"

The program will loop through that string and replace "my" with "your" and "me" with "you"
and then prepend the qualifier to the replacement string.
So, my teacher hates me becomes "Why do you say that your teacher hates you?" 

"""

Question = True
while Question:
  answer = input("Therapist: Good day. What is your problem? Enter your response here or Q to quit: ")

  print("User: " + answer )

  mod_answer = answer.replace(".","")
  answer_list = mod_answer.split()
  

  modified = ""
  for word in answer_list:
    if word.lower() == "i":
      modified += "you"
    elif str.lower(word) == "me":
      modified += "you"
    elif str.lower(word) == "my":
      modified += "your"
    elif str.lower(word) == "am":
      modified += "are"
    else:
      modified += word.lower()
    modified += " " # after every word, add a space

  modified2 = modified[:-1] # remove trailing space

  if str.lower(answer) == 'q' or str.lower(answer) == "i am feeling great":
    # we break the loop to quit the program
    Question = False
  else:
    # therapist says
    print("Therapist: Why do you say that " + modified2 + "?")

print("Therapist: Thanks, we're done!")
