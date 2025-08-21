nums = [3, 7, 1, 9, 5]

smallest = float('inf')
second_smallest = float('inf')

for number in nums:
    if number < smallest:
        second_smallest = smallest   # shift old smallest
        smallest = number            # new smallest
    elif number < second_smallest and number != smallest:
        second_smallest = number     # update with new second smallest

print("Smallest:", smallest)
print("Second Smallest:", second_smallest)
