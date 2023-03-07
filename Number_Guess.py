import random

top_of_range = input("Type A Number:- ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please Input Number Larger Than Next time...')
        quit()
else:
    print('Please Type The Number Next Time..')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make A Guess...")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please Enter Number Next Time...')
        continue

    if user_guess == random_number:
        print("You Got It..!!")
        break
    elif user_guess > random_number:
        print("You Were Above The Number..!!")
    else:
        print("You Were Below The Number..!!")

print("You Got It In",guesses,"Guesses")