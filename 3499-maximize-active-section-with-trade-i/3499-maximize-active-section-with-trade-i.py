class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        n = len(s)
        initial_ones = s.count("1")

        # Run-length encoding
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        max_gain = 0

        # Pattern: 0-run, 1-run, 0-run
        for i in range(1, len(runs) - 1):
            if (runs[i][0] == '1' and
                runs[i - 1][0] == '0' and
                runs[i + 1][0] == '0'):

                gain = runs[i - 1][1] + runs[i + 1][1]
                max_gain = max(max_gain, gain)

        return initial_ones + max_gain