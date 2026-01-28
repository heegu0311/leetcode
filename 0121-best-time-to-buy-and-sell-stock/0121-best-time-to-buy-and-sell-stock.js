/**
 * @param {number[]} prices
 * @return {number}
 */
function maxProfit(prices) {
    // 초기값을 어떻게 설정해야 할까요?
    let minPrice = Infinity;
    let maxProfit = 0;
    
    // 루프 안에서는?
    for (let i = 0; i < prices.length; i++) {
        const price = prices[i];
        const profit = price - minPrice;
        // 1. minPrice 업데이트: ?
        if(price < minPrice) minPrice = prices[i];
        // 2. maxProfit 업데이트: ?
        if(profit > maxProfit) maxProfit = profit;
    }
    
    return maxProfit;
}