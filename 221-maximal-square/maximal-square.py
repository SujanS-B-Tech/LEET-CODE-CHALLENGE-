class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        mx = 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                    if dp[i][j] > mx:
                        mx = dp[i][j]

                elif matrix[i][j] == "0":
                    dp[i][j] = 0

                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )

                    if dp[i][j] > mx:
                        mx = dp[i][j]

        return mx * mx