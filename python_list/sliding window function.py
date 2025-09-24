#sliding window function
def maxSumSubarray(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])  # first window
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i-k]  # slide window
        max_sum = max(max_sum, window_sum)

    return max_sum

print(maxSumSubarray([2,1,5,1,3,2], 3))
