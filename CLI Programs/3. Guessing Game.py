import os
import random

Scope = input("Do you want default range of (1-100) or not (y or n): ").lower()
program_range = 0
if Scope == "y":
    print("Define your own Scope")
    custom_scope_start = int(input("Where will it begin: "))
    custom_scope_end = int(input("Where will it end: "))
    custom_range = range(custom_scope_start, custom_scope_end+1)
    program_range = custom_range
else:
    print("Default Range has been Selected")
    default_start = 1
    default_end = 100
    default_range = range(default_start, default_end+1)
    program_range = default_range
os.system("cls")

def main():
    resume = True
    attempt_count = 0
    round = 1
    print (f"Round {round}")
    system_number = random.choice(program_range)
    while resume:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Enter a valid number")
            continue
        attempt_count += 1
        if guess == system_number:
            print(f"Congrats you guessed the correct number {system_number}")
            print(f"Your attempt count is {attempt_count}")
            Confirm = input("Will you like to continue(y or n): ").lower()
            if Confirm == "n":
                print("Thanks for playing")
                break
            else:
                system_number = random.choice(program_range)
                attempt_count = 0
                round += 1
                os.system("cls")
                print (f"Round {round}")
                continue
        elif guess > system_number:
            print("Your guess is bigger")
        elif guess < system_number:
            print("Your Guess is smaller")
    
main()
    



