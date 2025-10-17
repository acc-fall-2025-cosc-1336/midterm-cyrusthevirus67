from question_b import get_sum_of_evens

def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ").lower()
        if user_input == 'q':
            break
        try:
            num = int(user_input)
            print(f"Sum of even numbers up to {num}: {get_sum_of_evens(num)}")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
