def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

arr = [12, 35, 1, 10, 34, 1]
print(linear_search(arr, 10))  # Output: 3
print(linear_search(arr, 99))  # Output: -1
