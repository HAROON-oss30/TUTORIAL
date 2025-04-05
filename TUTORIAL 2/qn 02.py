# 2. Remove characters at odd index positions
s = input("Enter a string: ")
new_s = "".join(s[i] for i in range(0, len(s), 2))
print("String after removing odd index characters:", new_s)
