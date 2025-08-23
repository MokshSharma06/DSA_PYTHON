arr = [10, 20, 30, 40, 50, 60, 70]
d = 3

def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end -=1

def right_reverse(arr,d):
    n=len(arr)
    d=d%n
    reverse(arr,0,n-1) # reversed entire row 
    reverse(arr,0,d-1) # reverse the d elements
    reverse(arr,d,n-1) # reverse remaining elements
    return arr



print(right_reverse(arr,d))
