def maxSubarrayOfSizeK(arr, k):
    maxSum = 0
    for i in range(0, k):
        maxSum += arr[i]

    currSum = maxSum
    for i in range(k, len(arr)):
        currSum = currSum - arr[i - k] + arr[i]
        maxSum = max(maxSum, currSum)

    return maxSum
