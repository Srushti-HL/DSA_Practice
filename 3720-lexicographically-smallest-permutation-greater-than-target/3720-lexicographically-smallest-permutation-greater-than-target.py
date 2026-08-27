class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            # Use the same character as target if possible
            if count[t] > 0:
                count[t] -= 1
                ans.append(target[i])
                continue

            # Same character is unavailable.
            # Try the smallest character greater than target[i].
            for c in range(t + 1, 26):
                if count[c] > 0:
                    result = ans + [chr(c + ord('a'))]
                    count[c] -= 1

                    # Put remaining characters in sorted order
                    for x in range(26):
                        result.extend([chr(x + ord('a'))] * count[x])

                    return ''.join(result)

            # Cannot make current position greater,
            # so we need to backtrack.
            break

        # We matched target completely.
        # Therefore, we need to backtrack to make it strictly greater.
        for i in range(len(ans) - 1, -1, -1):
            old = ord(ans[i]) - ord('a')
            count[old] += 1

            t = ord(target[i]) - ord('a')

            # Find smallest character greater than target[i]
            for c in range(t + 1, 26):
                if count[c] > 0:
                    result = ans[:i] + [chr(c + ord('a'))]
                    count[c] -= 1

                    # Fill remaining characters in ascending order
                    for x in range(26):
                        result.extend([chr(x + ord('a'))] * count[x])

                    return ''.join(result)

        return ""