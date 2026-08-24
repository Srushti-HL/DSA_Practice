class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # prefix sum
        total = 0
        prefix = [0] * n

        for i in range(n):
            total += stones[i]
            prefix[i] = total

        # Start from taking the first n-1 stones
        ans = prefix[n - 1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans