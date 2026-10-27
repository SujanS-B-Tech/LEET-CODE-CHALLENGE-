class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        ans = [""] * m

        ans[0] = "." * n

        for i in range(1, m):
            ans[i] = "#" * (n - 1) + "."

        return ans