class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        size = 1
        while size < n:
            size <<= 1

        tree = [[1, [0] * k] for _ in range(2 * size)]

        def make(v):
            v %= k
            cnt = [0] * k
            cnt[v] = 1
            return [v, cnt]

        def merge(A, B):
            p, a = A
            q, b = B

            cnt = a[:]

            for r in range(k):
                cnt[(p * r) % k] += b[r]

            return [(p * q) % k, cnt]

        for i, x in enumerate(nums):
            tree[size + i] = make(x)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

        def update(pos, val):
            i = size + pos
            tree[i] = make(val)

            i >>= 1
            while i:
                tree[i] = merge(tree[i << 1], tree[i << 1 | 1])
                i >>= 1

        def query(l, r):
            left = [1, [0] * k]
            right = [1, [0] * k]

            l += size
            r += size + 1

            while l < r:
                if l & 1:
                    left = merge(left, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right = merge(tree[r], right)

                l >>= 1
                r >>= 1

            return merge(left, right)[1]

        ans = []

        for idx, val, start, x in queries:
            update(idx, val)
            ans.append(query(start, n - 1)[x])

        return ans