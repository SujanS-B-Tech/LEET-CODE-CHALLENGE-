class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        depth = 0

        for i in range(n):
            ch = s[i]

            if ch == '(':
                depth += 1
                ans[i] = depth % 2
            elif ch == ')':
                ans[i] = depth % 2
                depth -= 1

        return ans