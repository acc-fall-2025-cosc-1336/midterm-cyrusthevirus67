from question_c import get_random_number

def main():
    print("Guess the number (1–5). Type 'q' to quit.")

    while True:
        target = get_random_number()
        while True:
            guess = input("Enter your guess: ").lower()
            if guess == 'q':
                print("Goodbye!")
                return
            try:
                guess_num = int(guess)
            except ValueError:
                print("Please enter a number between 1 and 5.")
                continue

            if guess_num == target:
                print("Correct! 🎉 Generating a new number...\n")
                break
            else:
                print("Wrong! Try again.")

if __name__ == "__main__":
    main()
