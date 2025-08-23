def reverse(arr, start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

arr =[1,2,3,4,5,6,7,8,9]
d=2


def left_rotate(arr,d):
    n=len(arr)
    d = d % n #Prevents errors when d > n. 
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

print(left_rotate(arr,d))

# Suppose we have an array of length n = 9: arr = [1,2,3,4,5,6,7,8,9]
# If we want to rotate left by d = 2, answer is: [3,4,5,6,7,8,9,1,2]
# But what if someone says rotate left by d = 11? 
# rotate by 9 → array unchanged , Rotating by 11 is the same as rotating by 11 % 9 = 2.
# so we use d % n  i.e 11 %9 =2 only 2 rotations needed.