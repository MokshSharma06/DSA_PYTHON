def kadane(arr):
    current_sum=0
    maximum_sum=float('-inf')

    for num in arr:
        current_sum+=num
        maximum_sum = max(current_sum,maximum_sum)
        if current_sum < 0:
            current_sum=0
    return maximum_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(kadane(arr))


# more robust and stick to it 

def robust(arr):
    current_sum = arr[0]
    maximum_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(robust(arr))
