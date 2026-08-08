class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # suf[i] = minimum position in word2 that can still
        # be matched using word1[i:]
        suf = [0] * (n + 1)
        suf[n] = m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suf[i] = j + 1

        ans = [0] * m

        changed = False
        j = 0

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:

                ans[j] = i
                j += 1

            # Use the one allowed mismatch
            elif not changed and suf[i + 1] <= j + 1:

                ans[j] = i
                changed = True
                j += 1

        if j == m:
            return ans

        return []