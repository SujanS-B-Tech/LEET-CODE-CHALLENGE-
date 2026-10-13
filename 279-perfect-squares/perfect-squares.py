class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            min_val = float('inf')

            for j in range(1, int(i ** 0.5) + 1):
                remainder = i - j * j
                min_val = min(min_val, dp[remainder])
            dp[i] = min_val + 1

        return dp[n]