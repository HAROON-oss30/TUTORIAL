# 10. Password validity check
p = input("Enter password: ")
if (any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(c in "$#@" for c in p) and len(p) >= 6):
    print("Valid Password")
else:
    print("Invalid Password")
