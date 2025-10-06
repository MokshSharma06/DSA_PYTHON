nums = [3, 1, 2, 5, 4]

def pree(nums):
        prefix = [0] * len(nums)
        # initialize same size list
        prefix[0]=nums[0]

        for i in range(1,len(nums)):
                prefix[i]=prefix[i-1]+nums[i]
        print(prefix)

print(pree(nums))


