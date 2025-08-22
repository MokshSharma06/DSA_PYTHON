# Remove Duplicates but Keep Order O(n) time

nums = [3, 7, 1, 9, 5, 3, 7, 1, 3]
seen = set()
unique_list=[]

for number in nums:
    if number not in seen:
        unique_list.append(number)
        seen.add(number)

print(unique_list)

# brute force method ( its usally slower as it uses linear appraoch) O(n^2)

for number in nums:
    if number not in unique_list:
        unique_list.append(number)

print(unique_list)