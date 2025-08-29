# Find the key with the maximum value

scores = {"A": 50, "B": 80, "C": 65, "D": 90}

max = max(scores,key=scores.get)
print(max , scores[max])