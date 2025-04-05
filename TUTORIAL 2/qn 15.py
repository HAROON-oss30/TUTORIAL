# 15. Compute nCr using factorial function
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def compute_nCr():
    n = int(input("Enter value of n: "))
    r = int(input("Enter value of r: "))
    print(f"nCr({n}, {r}) =", factorial(n) // (factorial(r) * factorial(n - r)))
