def partition(arr):
    pivot = arr[0]
    left = arr[1]
    right= len(arr)-1

    while True:
        while left<=right and arr[left]<=pivot:
            left+=1
        while left<=right and arr[left]>=pivot:
            right-=1
        if left > right:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]

    arr[0],arr[right]=arr[right],arr[0]
    print("After partition, pivot =", pivot, "Array:", arr)
    return right  # return pivot index



arr = [7, 8, 1, 6]
pivot_index = partition(arr)
print("Pivot fixed at index:", pivot_index)