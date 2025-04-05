# 11. Convert decimal to binary


n = int(input("Enter a decimal number: "))
bin_n = ""
while n > 0:
    bin_n = str(n % 2) + bin_n
    n //= 2
print("Binary representation:", bin_n)
