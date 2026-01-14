def stock_profit_loss(prices):
    total=0
    for i in range(1,len(prices)):
        total+=prices[i]-prices[i-1]
    return total




prices=[100,120,90,95]
print(stock_profit_loss(prices))
