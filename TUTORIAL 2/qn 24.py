def find_mode():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    
    max_freq = max(freq.values())
    mode = [num for num, count in freq.items() if count == max_freq]
    
    print("Mode:", mode)

find_mode()
