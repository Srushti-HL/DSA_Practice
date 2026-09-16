class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]

        # 0 segments can always be chosen in exactly 1 way
        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(n):
                
                # Add dp[i-1][j-1] to the prefix sum
                if i > 0:
                    prefix = (prefix + dp[i - 1][j - 1]) % MOD

                # Either:
                # 1. Don't end a segment at i
                # 2. End the last segment at i
                dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + prefix
                dp[i][j] %= MOD

        return dp[n - 1][k]