# 26. Separate integers, floats, and strings into different lists
def separate_types():
    data = input("Enter mixed data (e.g. 1 hello 3.14): ").split()
    integers = [int(x) for x in data if x.isdigit()]
    floats = [float(x) for x in data if '.' in x and x.replace('.', '').isdigit()]
    strings = [x for x in data if not x.isdigit() and not x.replace('.', '').isdigit()]
    print("Integers:", integers)
    print("Floats:", floats)
    print("Strings:", strings)

separate_types()
