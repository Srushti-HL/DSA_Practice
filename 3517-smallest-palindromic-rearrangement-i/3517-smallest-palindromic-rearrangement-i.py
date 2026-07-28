from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        middle = ""

        # Characters are lowercase English letters.
        for ch in sorted(freq.keys()):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        left = "".join(left)
        right = left[::-1]

        return left + middle + right