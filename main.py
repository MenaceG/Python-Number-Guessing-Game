import random

random_number = random.randint(0, 10)
lives = 0

difficulty = {"Hard" "Medium" "Easy"}

difficulty = input("Select Difficulty:" + "\nHard- " + "\nMedium- " + "\nEasy- " + "\nChoose: ")
if difficulty.islower():
    difficulty = difficulty.capitalize()

if difficulty != difficulty.isalpha() and difficulty not in ["Easy", "Medium", "Hard"]:
    print("Choose Correct Difficulty")
    
if difficulty == "Hard":
    lives = 1
if difficulty == "Medium":
    lives = 3
if difficulty == "Easy":
    lives = 5


print(random_number) 
print(lives)

while lives != 0:
    user_input = int(input("Guess The Number: "))

    if user_input == random_number:
        print("You Guessed The Right Number: ")
        break

    elif user_input != random_number:
        print("Wrong Guess, Try Again.", lives-1, "lives left")
        lives -= 1
        
    if lives == 0:
        print("You Lost", lives, "lives left")

