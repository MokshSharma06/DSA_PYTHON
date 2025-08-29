# Find the key with the minimum value

scores = {"A": 50, "B": 80, "C": 65, "D": 90}

min = min(scores,key=scores.get)
print(min , scores[min])