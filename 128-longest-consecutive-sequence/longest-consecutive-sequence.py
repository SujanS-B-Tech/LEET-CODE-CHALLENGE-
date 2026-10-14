class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        curr = 1
        last_small = None

        for num in nums:
            if last_small is not None and num == last_small + 1:
                curr += 1
                last_small = num
            elif num != last_small:
                curr = 1
                last_small = num

            longest = max(longest, curr)

        return longest