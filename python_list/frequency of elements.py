#Count frequency of each element (using dictionary / hashmap)

nums = [3, 7, 1, 9, 5, 3, 7, 1, 3]

freq={}

for number in nums:
    freq[number]=freq.get(number,0)+1

print("frequencies :", freq)