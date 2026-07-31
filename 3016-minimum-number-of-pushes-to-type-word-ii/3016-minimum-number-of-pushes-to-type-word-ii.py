from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0

        for i, count in enumerate(freq):
            cost = (i // 8) + 1
            ans += count * cost

        return ans