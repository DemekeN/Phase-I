"""Zork is a famous text-only adventure game for the computer. Users would type commands and navigate the rooms of a castle.
The following application asks the user what direction they wish to travel in. Once they tell you the direction, move them to the next room and tell them what is in it and what direction the other exits are.
"""
import string
loop = 3
while loop == 3:
    print("---------------------------------------------------------")
    print("Welcome to Zork - which direct you to the appropriate room you like to go.")
    print("---------------------------------------------------------")
    print("Front room and Library are next to you ")
    print("(S1 , w3 and e4 leads you to front room and e2 & n5 will get you to library.)")
    print("There is piano in front room  and spiders in library.")
    #First Screen and Input
    first = input("Where do you want to go? ")
    if first.lower() == "library":
        print("---------------------------------------------------------")
        print("Hmm that is easy: First take e2 and then n5, once you open the door you will see Spider in the left side")
        loop = 4
        if first.lower() == "front room":
            print("---------------------------------------------------------")
            print("Opening the room reveals a piano.")
            loop = 4
            if first.lower() == "kitchen":
                print("---------------------------------------------------------")
                print("The door is boarded if you open you will find bats and rooms w2 & n7 are next")
                loop = 4
                if first.lower() == "dinning room":
                    print("---------------------------------------------------------")
                    print("First open door of room s3 and you will see dust and empty box inside")
                    loop = 4
                if first.lower() == "vault":
                    print("---------------------------------------------------------")
                    print("The boards are securely fastened.")
                    loop = 4
                    if first.lower() == "parlor":
                        print("---------------------------------------------------------")
                        print("The house is a beautiful colonial house which is painted white. Open door for room w6, s4 and you will see treasure chest")
                        loop = 4
                        if first.lower() == ("secret room"):
                            print("---------------------------------------------------------")
                            print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a piles of gold. door of room w6 will get you there ")
                            loop = 4
                        else:
                            print("---------------------------------------------------------")
                            loop = 4
                            loop = 4
                            print("---------------------------------------------------------")
                            print("Welcome to Zork - The Unofficial Python Version.")
