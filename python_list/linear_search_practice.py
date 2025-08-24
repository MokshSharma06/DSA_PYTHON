arr= [20, 35, 15, 40, 50, 10]

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
print(linear_search(arr,40))


# Binary Practice Now 
arr = [5, 10, 15, 20, 25, 30, 35, 40]

def binary_search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low =mid+1
        else:
            high =mid-1
    return "not found"
    

print(binary_search(arr,25))