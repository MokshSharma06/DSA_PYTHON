# Find all duplicates (unique duplicate values only)

nums = [3, 7, 1, 9, 5, 3, 7, 1, 3]
duplicates =[]

for number in nums:
    if nums.count(number) >1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate elements:", duplicates)