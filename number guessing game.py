import random


secret = random.randint(1, 50)
attempts = 5

print("NUMBER GUESSING GAME")
print("I have picked a secret number between 1 and 50.")
print("Can you guess it within 5 attempts")

while attempts > 0:
    print("\nRemaining lives: ", end="")
    for i in range(attempts):
        print()
    try:
        guess = int(input("Enter your guess:"))
    except ValueError:
        print("Please enter a valid number.")
        continue
      
    if guess == secret:
        print("Congratulations! You guessed the secret number.")
        break
    attempts -= 1

    if attempts > 0:
        difference = abs(secret - guess)

        if difference >= 20:
            print("Hint: Ice cold...")
        elif difference >= 10:
            print("Hint: Cold...")
        elif difference >=5:
            print("Hint: Warm...")
        else:
            print("Hint: Hot!! You are very close!!")
if attempts == 0:
    print("\n--------------------------")
    print("GAME OVER! You ran out of attempts.")
    print("The secret number was:", secret)
    print("--------------------------")