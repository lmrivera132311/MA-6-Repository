#In this project, I've learned using the class objects from the previous assessment, and using it to roll a die and having it land on a random side. Equally, I've used this to create a randomly generated ficticious lottery ticket number. (Please don't sue for false information)

import random
import string

class Die:
#In these lines of code I've declared what a die is and how many sides it should have. A normal amount of six. 
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
#Here, I've declared how many times it should roll (once) and where it should land, in this case it being on only one side. 
        return random.randint(1, self.sides)

def simulate_die_rolls():
#Here I've now allowed the program to learn to roll the six sideed die 10 times for a more varied result
    die = Die()
    print(" Rolling a 6-sided die 10 times:")
    for i in range(10):
        print(f"Roll {i+1}: {die.roll_die()}")
    print()

def generate_lottery_ticket():
#Similar to what I've done with the six sided die, I've declared a class for the lottery ticket, declared the pool of numbers it should have, and the desirable result
    numbers = list(range(10))  # 0 through 9
    letters = list(string.ascii_uppercase[:5])  # A, B, C, D, E
    lottery_pool = numbers + letters
    winning_ticket = random.sample(lottery_pool, 4)
    print("Lottery Winning Ticket:")
    print(f"Any ticket matching these four numbers or letters wins a prize: {winning_ticket}")

if __name__ == "__main__":
    simulate_die_rolls()
    generate_lottery_ticket()
