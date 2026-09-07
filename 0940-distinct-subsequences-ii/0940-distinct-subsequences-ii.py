class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * (len(s) + 1)
        dp[0] = 1  # empty subsequence

        last = {}

        for i, ch in enumerate(s, 1):
            dp[i] = (2 * dp[i - 1]) % MOD

            if ch in last:
                dp[i] = (dp[i] - dp[last[ch] - 1]) % MOD

            last[ch] = i

        return (dp[len(s)] - 1) % MOD