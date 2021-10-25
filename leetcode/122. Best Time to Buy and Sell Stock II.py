'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
# 여러 번의 거래로 낼 수 있는 최대 이익을 산출
# 1일대 사서 5일때 팔아 4의 이익을 얻고 3일대 사서 6일때 팔아 3의 이익을 얻는다 둘을 합하면 7이 된다.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
'''

def maxProfit(self, prices):
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices) -1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result
# Runtime: 75 ms, faster than 19.63% of Python online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 14.4 MB, less than 89.03% of Python online submissions for Best Time to Buy and Sell Stock II.


def maxProfit(self, prices):
    # 0보다 크면 무조건 합산
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) -1))
# Runtime: 55 ms, faster than 42.17% of Python online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 14.5 MB, less than 42.66% of Python online submissions for Best Time to Buy and Sell Stock II.