class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            reverse_position = 26 - (ord(ch) - ord('a'))
            string_position = i + 1

            ans += reverse_position * string_position

        return ans