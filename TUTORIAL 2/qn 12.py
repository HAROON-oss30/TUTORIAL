# 12. Convert binary to decimal

b = input("Enter a binary number: ")
dec = sum(int(b[i]) * (2 ** (len(b) - 1 - i)) for i in range(len(b)))
print("Decimal representation:", dec)
