sentence = "i love data and i love python"

# Split sentence into words
words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# .get()
# dict.get(key, default_value)
# Looks for key inside the dictionary.

# If key exists → returns its value.

# If key doesn’t exist → returns default_value.

