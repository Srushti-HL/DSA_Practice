class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = []

        for i in range(26):
            if count[i] % 2 == 1:
                odd.append(i)

        if len(odd) > 1:
            return ""

        # Count of characters needed for left half
        half_count = [c // 2 for c in count]

        m = n // 2

        def build_palindrome(left):
            if n % 2 == 1:
                middle = chr(odd[0] + ord('a'))
                return left + middle + left[::-1]
            else:
                return left + left[::-1]

        target_half = target[:m]

        # Check if target's first half can be constructed
        remaining = half_count[:]
        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        # If target_half is possible, check its palindrome
        if possible:
            left = target_half
            palindrome = build_palindrome(left)

            if palindrome > target:
                return palindrome

        # Find the next lexicographically greater half
        for i in range(m - 1, -1, -1):

            remaining = half_count[:]

            # Match prefix target_half[0:i]
            valid = True

            for j in range(i):
                idx = ord(target_half[j]) - ord('a')

                if remaining[idx] == 0:
                    valid = False
                    break

                remaining[idx] -= 1

            if not valid:
                continue

            # Find smallest character greater than target_half[i]
            current = ord(target_half[i]) - ord('a')

            for c in range(current + 1, 26):

                if remaining[c] > 0:
                    remaining[c] -= 1

                    # Put remaining characters in sorted order
                    suffix = ""

                    for k in range(26):
                        suffix += chr(k + ord('a')) * remaining[k]

                    left = (
                        target_half[:i]
                        + chr(c + ord('a'))
                        + suffix
                    )

                    return build_palindrome(left)

        return ""