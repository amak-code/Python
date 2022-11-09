"""A number-guessing game."""

# Put your code here
import random

print("Hello player welcome to our guessing game")

name = input("what is your name: ")
user_range_low_num = int(input("Please enter the lower range number! "))
user_range_high_num = int(input("Please enter the higher range number! "))

print(f"{name} , I'm thinking of a number between {user_range_low_num} and {user_range_high_num}. Try to guess my number.")
randomNumber = random.randint(user_range_low_num, user_range_high_num)
print(f"Shh don't tell yourself this is the number {randomNumber}")
guess = 0
low_num = 1
isGameOver = False
min_num_of_guesses = 0
totalGuesses = 0
max_try = 10
while not isGameOver:
    guess = int(input("Your guess? "))

    totalGuesses = totalGuesses + 1

    if guess > 100 or guess < 1 and totalGuesses < 10:
        print("please guess again your guess was out of range (1-100)")
        guess = int(input("Your guess? "))

    if guess < randomNumber and totalGuesses < 10:
        print("Your guess is too low, try again.")
      
    elif guess > randomNumber and totalGuesses < 10:
        print("Your guess is too high, try again.")
        
    else: 
        if totalGuesses < 10:
           
            if min_num_of_guesses > totalGuesses or min_num_of_guesses==0:
                min_num_of_guesses = totalGuesses
            print(f"Well done, {name}! You found my number in {totalGuesses} tries!") 
            answer = input("Would you like to play again?")
            if answer.lower() == 'no':
                isGameOver = True
                print(f"Your best score is {min_num_of_guesses}")
            else:
                totalGuesses = 0
                randomNumber = random.randint(user_range_low_num, user_range_high_num)
                print(f"Shh don't tell yourself this is the number {randomNumber}") 
        else:
            print("Too many tries!")
            answer = input("Would you like to play again?")
            if answer.lower() == 'no':
                isGameOver = True
                print(f"Your best score is {min_num_of_guesses}")
            else:
                totalGuesses = 0
                randomNumber = random.randint(user_range_low_num, user_range_high_num)
                print(f"Shh don't tell yourself this is the number {randomNumber}")



