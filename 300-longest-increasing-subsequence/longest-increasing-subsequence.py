class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for x in nums:
            i = bisect_left(lis, x)
            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x
        return len(lis)