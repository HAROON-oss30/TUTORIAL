# 30. Remove duplicate elements from a list
def remove_duplicates_keep_first():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    seen = set()
    unique_numbers = [num for num in numbers if not (num in seen or seen.add(num))]
    print("List without duplicates:", unique_numbers)

remove_duplicates_keep_first()
