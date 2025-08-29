# Sort dictionary by values
d = {"apple": 40, "banana": 10, "mango": 50}

variable = sorted(d.items(),key=lambda x:x[1], reverse=True)
print(variable)


# Sort a list ascending
nums = [5, 2, 9, 1]
print(sorted(nums))  

# Sort a list descending
print(sorted(nums, reverse =True))

# Sort by custom key (length of string)

words = ["apple", "dog", "banana"]

print(sorted(words ,key=len))

# sort using ages
people = [("Alice", 25), ("Bob", 19), ("Charlie", 30)]
print(sorted(people,key= lambda x:x[1], reverse= False)) 