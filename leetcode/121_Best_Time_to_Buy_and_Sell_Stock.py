def maxProfit(prices):
    minNum = 10^5+1
    for i in prices:
        if minNum > i:
            minNum = i

    idx = prices.index(minNum)
    maxNum = -1
    for i in range(idx+1, len(prices)):
        if maxNum < prices[i]:
            maxNum = prices[i]

    result = maxNum-minNum
    if result > 0:
        return result
    else:
        return 0

#prices = [7,3,1,5,3,6,4]
prices = [7, 3, 1]

print(maxProfit(prices))