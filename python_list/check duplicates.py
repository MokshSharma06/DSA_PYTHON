# Check if duplicates exist

nums = [3, 7, 1, 9, 5, 3, 7, 1, 3]
if len(nums)!= len(set(nums)):
    print ("Duplicate exists" )
else:
    print("doesnt exists")

print(len(nums))
print(set(nums))