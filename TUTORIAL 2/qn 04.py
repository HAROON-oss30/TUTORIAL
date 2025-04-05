# 4. Replace spaces with * or wrap in $
s = input("Enter a string: ")
if " " in s:
    s = s.replace(" ", "*")
else:
    s = "$" + s + "$"
print("Modified string:", s)
