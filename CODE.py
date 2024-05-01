# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Importing the random module
import random

# Getting user input for their choice
user_choice = int(input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors "))

# Creating a list of hand gestures
hand = [rock, paper, scissors]
num_of_hand = len(hand)

# Generating a random choice for the computer
random_hand = random.randint(0, num_of_hand - 1)
computer_choice = hand[random_hand]

# Determining the winner based on user and computer choices
if user_choice == 0 and random_hand == 2:
    print(f"{rock}\nYou win\n{scissors}\nComputer loses")
elif user_choice == 2 and random_hand == 0:# ASCII art for rock, paper, and scissors

ALTERNATE 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Importing the random module
import random

# Getting user input for their choice
user_choice = int(input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors "))

# Creating a list of hand gestures
hand = [rock, paper, scissors]
num_of_hand = len(hand)

# Generating a random choice for the computer
random_hand = random.randint(0, num_of_hand - 1)
computer_choice = hand[random_hand]

# Determining the winner based on user and computer choices
if user_choice == 0 and random_hand == 2:
    print(f"{rock}\nYou win\n{scissors}\nComputer loses")
elif user_choice == 2 and random_hand == 0:
    print(f"{rock}\nYou lose\n{scissors}\nComputer wins")
elif user_choice == 1 and random_hand == 0:
    print(f"{paper}\nYou win\n{rock}\nComputer loses")
elif user_choice == 0 and random_hand == 1:
    print(f"{rock}\nYou lose\n{paper}\nComputer wins")
elif user_choice == 2 and random_hand == 1:
    print(f"{scissors}\nYou win\n{paper}\nComputer loses")
elif user_choice == 1 and random_hand == 2:
    print(f"{paper}\nYou lose\n{scissors}\nComputer wins")
elif user_choice == random_hand:
    print(f"{hand[user_choice]}\nIt's a draw\n{hand[random_hand]}\nComputer chose")
else: 
    print("Please enter a number between 0 and 2")

    print(f"{rock}\nYou lose\n{scissors}\nComputer wins")
elif user_choice == 1 and random_hand == 0:
    print(f"{paper}\nYou win\n{rock}\nComputer loses")
elif user_choice == 0 and random_hand == 1:
    print(f"{rock}\nYou lose\n{paper}\nComputer wins")
elif user_choice == 2 and random_hand == 1:
    print(f"{scissors}\nYou win\n{paper}\nComputer loses")
elif user_choice == 1 and random_hand == 2:
    print(f"{paper}\nYou lose\n{scissors}\nComputer wins")
elif user_choice == random_hand:
    print(f"{hand[user_choice]}\nIt's a draw\n{hand[random_hand]}\nComputer chose")
else: 
    print("Please enter a number between 0 and 2")
