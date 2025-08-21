#find the biggest number from the list
nums = [3, 7, 2, 9, 5]

biggest =nums[0]
for number in nums:
    if number > biggest:
        biggest = number

print(f" the largest number is :", biggest)