import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        f = {}

        for i in nums:
            f[i] = f.get(i, 0) + 1

        heap = []

        for i, c in f.items():
            heapq.heappush(heap, (c, i))

            if len(heap) > k:
                heapq.heappop(heap)

        return [i for c, i in heap]