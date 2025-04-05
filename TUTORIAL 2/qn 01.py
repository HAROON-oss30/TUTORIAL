# 1. Remove all vowels from a string

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_s = "".join(c for c in s if c not in vowels)
print(new_s)
