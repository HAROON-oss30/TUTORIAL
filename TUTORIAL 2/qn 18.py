# 18. Factorial using recursion
def recursive_factorial(n):
    return 1 if n == 0 else n * recursive_factorial(n - 1)

def compute_factorial():
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {recursive_factorial(num)}")

compute_factorial()
