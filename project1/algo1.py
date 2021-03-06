
        
def algo1(arr=[]):
    """
    Description: Algorithm 1 - Enumeration
       Computes the sum of all possible subarrays and returns the array with the
       largest sum.  Stores the largest sum found so far in the maxSum variable.
    Input: arr - an array of ints
    Output: Returns max subarray and max sum in a tuple
    Complexity: O(n^3)
    """

    #if the array is empty, return 0
    if len(arr) == 0:
        return 0, 0, 0
    
    #if the array only has one element, return that value of that element
    elif len(arr) == 1:
        return arr, arr[0]

    maxSum = arr[0]  #the largest sum of a subarray of arr
    start = 0        #the beginning index for a subarray of arr
    stop = 0         #the end index for a subarray arr

    #compute the sum for all possible pairs of indices (i,j) such that 0<=i<j
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            curSum = sum(arr[i:j+1])
            if curSum > maxSum:
                start = i
                stop = j
                maxSum = curSum

    #check to see if the last element in arr is larger than all other subarray sums
    #i.e. like for the array [-2,-5,-11,5]
    if arr[len(arr) - 1] > maxSum:
        maxSum = arr[len(arr) - 1]
        start = len(arr) - 1
        stop = len(arr) - 1
    
    return arr[start:stop+1], maxSum
