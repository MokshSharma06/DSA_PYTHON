numbers = [1,2,3,4,4,5,5]


def is_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False
        
            
print(is_duplicate(numbers))


def duplicates(numbers):
    hashmap={}
    result=[]
    for num in numbers:
        hashmap[num]=hashmap.get(num,0)+1
        
    for num in hashmap:
        if hashmap[num]>1:
            result.append(num)
    return result
    

print(duplicates(numbers))


def removeDuplicates(nums):  # if sorting allowed
    numbers.sort()
    n=len(nums)
    left=0
    right=left+1

    while right<n:
        if nums[left]==nums[right]:
            right+=1
        else:
            left+=1
            nums[left]=nums[right]
            right+=1
    return nums[:left+1]
    
print(removeDuplicates(numbers))

def remove_duplicates(nums): # not sorted
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
    
print(remove_duplicates(numbers))
    
