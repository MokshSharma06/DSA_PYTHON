nums = [4, 5, 4, 3, 5, 4, 4 ,4,2, 5]

def yoyo(nums):
    freq={}

    for numbers in (nums):
        freq[numbers]=freq.get(numbers,0)+1
    max_key = max(freq, key=freq.get)

    return (max_key)

print(yoyo(nums))