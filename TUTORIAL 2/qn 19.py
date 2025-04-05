# 19. nth Fibonacci number using recursion
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def compute_fibonacci():
    num = int(input("Enter n: "))
    print(f"{num}th Fibonacci number is {fibonacci(num)}")

compute_fibonacci()
