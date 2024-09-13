import pandas as pd
import re
import random

def main_menu():
    print("MAIN MENU")
    print("1. String Operation")
    print("2. Number Operation")
    print("3. EXIT")

def fn_email_validation(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def create_pyramid(n):
    for i in range(0, n):
        print("#" * i)
    for i in range(n, 0, -1):
        print("#" * i)

def write_lines_to_file(filename):
    lines = []
    print("Enter multiple lines of text (type 'DONE' on a new line to finish):")
    while True:
        line = input("")
        if line.strip().upper() == "DONE":
            break
        lines.append(line)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"File [{filename}] has been saved successfully!")

def fn_reverse_number():
    n = int(input("Enter a number: "))
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    print("Reversed number is:", reversed_num)

def fibo():
    n = int(input("Enter a number for series: "))
    a, b = 0, 1
    print(a, end=' ')
    for _ in range(n-1):
        c = a + b
        print(c, end=' ')
        a = b
        b = c
    print()

def fn_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fn_factorial(n-1)

def fn_random_number_generator():
    with open("100Numbers.txt", "w") as file:
        for _ in range(100):
            number = random.randint(1, 100)
            file.write(str(number) + " ")
    with open("100Numbers.txt", "r") as file:
        print(file.read())

def main():
    while True:
        main_menu()
        rchoice = input('\nEnter choice(1, 2 or 3): ')
        if rchoice == '1':
            while True:
                print("\nString Operations Menu")
                print("1. Email Validation")
                print("2. Create Pyramid")
                print("3. Write Lines to File")
                print("4. Return to Main Menu")
                choice = input('\nEnter choice (1-4): ')
                if choice == '1':
                    email = input("\nEnter an email address: ")
                    if fn_email_validation(email):
                        print(f"\nProvided email address [{email}] is valid")
                    else:
                        print(f"\nProvided email address [{email}] is not valid")
                elif choice == '2':
                    n = int(input("How many rows for the pyramid? "))
                    create_pyramid(n)
                elif choice == '3':
                    filename = "output2.txt"
                    write_lines_to_file(filename)
                elif choice == '4':
                    break
                else:
                    print('\nInvalid input!!!')
        elif rchoice == '2':
            while True:
                print("\nNumber Operations Menu")
                print("1. Reverse Number")
                print("2. Fibonacci Series")
                print("3. Factorial")
                print("4. Random Number Generator")
                print("5. Return to Main Menu")
                choice = input('\nEnter choice (1-5): ')
                if choice == '1':
                    fn_reverse_number()
                elif choice == '2':
                    fibo()
                elif choice == '3':
                    n = int(input("Enter a number to calculate factorial: "))
                    print(f"Factorial of {n} is {fn_factorial(n)}")
                elif choice == '4':
                    fn_random_number_generator()
                elif choice == '5':
                    break
                else:
                    print('\nInvalid input!!!')
        elif rchoice == '3':
            print('\nThanks for using the program!')
            break
        else:
            print('\nInvalid input!!!')

if __name__ == "__main__":
    main()