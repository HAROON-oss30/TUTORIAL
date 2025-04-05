# 28. Sort a list without built-in functions
def sort_list():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    def bubble_sort(lst):
        for i in range(len(lst)):
            for j in range(len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    print("Sorted list:", bubble_sort(numbers))
sort_list()
