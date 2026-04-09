import random
#generate a random number between 1 to 100
number = random.randint(1,100)

print ("welcome to the number guessing game!")
print ("i have selected a number between 1 to 100, can you guess it?")

while True:
    guess = int(input("enter your guesss:"))
    if guess < number:
        print ("too low! try again.")
    elif guess > number:
        print ("too high! try again.")
    else:
        print ("congratulation! you guessed the number correnctly.")
        break