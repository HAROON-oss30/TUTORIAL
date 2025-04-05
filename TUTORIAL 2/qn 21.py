# 21. Sum of all even numbers in a list
def sum_even_numbers():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Sum of even numbers:", sum(num for num in numbers if num % 2 == 0))


sum_even_numbers()
