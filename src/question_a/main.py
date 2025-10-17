from question_a import get_miles_per_hour

def main():
    try:
        kilometers = int(input("Enter kilometers: "))
        minutes = int(input("Enter minutes: "))
        result = get_miles_per_hour(kilometers, minutes)
        print(result)
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
