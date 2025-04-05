import math
# 27. Separate prime and composite numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def separate_primes():
    numbers = list(map(int, input("Enter positive integers separated by spaces: ").split()))
    primes = [n for n in numbers if is_prime(n)]
    composites = [n for n in numbers if n > 1 and not is_prime(n)]
    print("Primes:", primes)
    print("Composites:", composites)

separate_primes()
