rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n
'''
import random
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0:
  print("Great job, you beat the computer!\n")
elif user_choice == 2 and computer_choice == 1:
  print("Great job, you beat the computer!\n")
elif user_choice == computer_choice:
  print("Look at that, it's a TIE.\n")
else:
  print("Oh no, you lost to the computer. Better luck next time.\n")
