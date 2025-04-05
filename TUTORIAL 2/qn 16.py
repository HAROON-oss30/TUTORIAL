# 16. Menu-driven program for basic operations
def check_even_odd():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

def check_number():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

def generate_factors():
    num = int(input("Enter a number: "))
    factors = [i for i in range(1, num + 1) if num % i == 0]
    print("Factors:", factors)

def menu():
    while True:
        print("\n1. Check even or odd")
        print("2. Check positive, negative, or zero")
        print("3. Generate factors of a number")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            check_even_odd()
        elif choice == 2:
            check_number()
        elif choice == 3:
            generate_factors()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Try again.")
