# 29. Basic set operations
def set_operations():
    set1 = set(map(int, input("Enter first set of numbers: ").split()))
    set2 = set(map(int, input("Enter second set of numbers: ").split()))
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (set1 - set2):", set1 - set2)
set_operations()
