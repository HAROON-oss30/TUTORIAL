# 14. Compute nCr using factorial

def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)
n, r = map(int, input("Enter n and r: ").split())
print("nCr value:", factorial(n) // (factorial(r) * factorial(n - r)))
