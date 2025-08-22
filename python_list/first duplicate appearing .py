#Find first duplicate (appearing earliest)

nums = [3, 7, 1, 9, 5, 3, 7, 1, 3]
seen =set()
dup = None;

for number in nums:
    if number in seen:
        dup = number
        break
    seen.add(number)

print("First duplicate:", dup)