#5. Slice into odd and even index strings

s = input("Enter a string: ")
odd_chars = s[1::2]
even_chars = s[0::2]
print("Characters at odd indices:", odd_chars)
print("Characters at even indices:", even_chars)
