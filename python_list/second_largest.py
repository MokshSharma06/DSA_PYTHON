nums = [1,5,7,8,9,10,100,120,240,250]

largest = nums[1]

for number in nums:
    if number > largest:
        largest = number

print(f"largest is = ", largest)

second_largest = float('-inf')
for number in nums:
    if number != largest and number > second_largest:
        second_largest=number

print(f"second largest is = ",second_largest)