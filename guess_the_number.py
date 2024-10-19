import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempt = 0

    while True:
        guess = input("Guess: ")
        if guess.lower == 'exit':
            print("Thanks for Playing!")
            break
        try:
            guess = int(guess)
            attempt += 1
            if guess < number_to_guess:
                print("Too Low")
            elif guess > number_to_guess:
                print("Too High")
            else:
                print(f"Congratulations, You guessed the right number {guess} at {attempt}th attempt.")
                break
        except ValueError:
            print("Invalid Value")
        except ZeroDivisionError:
            print("0 not included, only from 1 to 100")

if __name__ == "__main__":
    guess_the_number()