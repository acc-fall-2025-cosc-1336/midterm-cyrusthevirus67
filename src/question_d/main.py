from question_d import get_fahrenheit

def main():
    print("Celsius to Fahrenheit Table")
    print("----------------------------")
    print("Celsius\tFahrenheit")
    print("----------------------------")

    for c in range(0, 21):  # 0 through 20
        f = get_fahrenheit(c)
        print(f"{c}\t{f}")

if __name__ == "__main__":
    main()
