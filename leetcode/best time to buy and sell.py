
def maxProfit(prices):
    max = 0;
    min = prices[0];
        
    for i in range(1,len(prices)):
        if prices[i] < min :
            min = prices[i]
            
        elif((prices[i] - min) > max):
            max = prices[i] - min
        
    return max;
#Prices=[1,3,5,3,7]
Prices=[7,1,5,3,6,4]
print(maxProfit(Prices))