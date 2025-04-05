# 9. Reverse first and second half separately
s = input("Enter a string: ")
half = len(s) // 2
first_half = s[:half][::-1]
second_half = s[half:][::-1]
print("Reversed halves combined:", first_half + second_half)
