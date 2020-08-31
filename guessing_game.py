import random

num = random.randint(1,100)

guesses = [0]

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:

    guess = int(input("I'm thinking of a number. What is that number? \nEnter your guess here: "))

    if guess <1 or guess >100:
        print('OUT OF BOUNDS!')
        continue
    if guess == num:
        print(f'Congratulations! You guessed the number in {len(guesses)} guesses')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num-guess) <=10:
            print('WARM!')
        else:
            print('COLD!')
    
    pass
