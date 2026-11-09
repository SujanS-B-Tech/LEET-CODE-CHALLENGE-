import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        free = list(range(k))
        busy = []
        cnt = [0] * k

        for i, t in enumerate(arrival):
            while busy and busy[0][0] <= t:
                _, j = heapq.heappop(busy)
                heapq.heappush(free, i + (j - i) % k)
            if not free:
                continue

            j = heapq.heappop(free) % k
            cnt[j] += 1
            heapq.heappush(busy, (t + load[i], j))

        mx = max(cnt)
        return [i for i, c in enumerate(cnt) if c == mx]