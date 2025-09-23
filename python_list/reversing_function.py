def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5]
reverse(arr,0,4)
print(arr)

#   while start < end → keep swapping until middle.

# arr[start], arr[end] = arr[end], arr[start] → swap the elements.

# start += 1, end -= 1 → move pointers inward.