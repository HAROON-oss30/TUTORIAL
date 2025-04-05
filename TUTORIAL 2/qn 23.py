# 23. Find the median of a list
def find_median():
    numbers = sorted(map(int, input("Enter numbers separated by spaces: ").split()))
    mid = len(numbers) // 2
    median = (numbers[mid] + numbers[mid - 1]) / 2 if len(numbers) % 2 == 0 else numbers[mid]
    print("Median:", median)

find_median()
