def bubblesort(arr):
    n=len(arr)

    for i in range(n):
        flag = False

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
            if not swapped:
                    break
    return arr

arr = [64, 25, 12, 22, 11]

print(bubblesort(arr))