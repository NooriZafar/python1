arr=[1,2,3,4,-5]
def maxsubarray(arr):
    dp=[0 for i in range(len(arr))]#create array of same size as arr with all zero values
    dp[0]=arr[0]
    for i in range(1,len(arr)):
        dp[i]=max(dp[i-1]+arr[i],arr[i])
    return max(dp)
print(maxsubarray(arr))
