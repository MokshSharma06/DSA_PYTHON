arr = [10, 20, 30, 40, 50, 60, 70, 80]

d = 4

def reverse (arr, start ,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

def left_rotate(arr,d):
    n=len(arr)
    d= d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

print(left_rotate(arr,d))
