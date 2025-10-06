nums = [3, 1, 2, 5, 4]

n =len(nums)
def suff(nums):
    suffix =[0]*n
    suffix[-1]=nums[-1]

    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]+ nums[i]

    return suffix

print(suff(nums))