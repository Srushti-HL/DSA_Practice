from math import factorial
from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        # Build half counts and middle character.
        half = [0] * 26
        middle = ""

        for ch, cnt in freq.items():
            idx = ord(ch) - ord("a")
            half[idx] = cnt // 2
            if cnt % 2:
                middle = ch

        max_k = 10**6 + 1

        # Compute number of distinct permutations of the current multiset.
        def count_permutations(counts):
            total = sum(counts)

            res = 1
            remaining = total

            # Compute multinomial coefficient incrementally:
            # total! / (c1! * c2! * ...)
            for c in counts:
                if c == 0:
                    continue

                # C(remaining, c)
                if c > remaining - c:
                    c2 = remaining - c
                else:
                    c2 = c

                comb = 1
                for i in range(1, c2 + 1):
                    comb = comb * (remaining - c2 + i) // i
                    if comb > max_k:
                        comb = max_k
                        break

                res *= comb
                if res > max_k:
                    res = max_k

                remaining -= c

            return res

        # Check whether k is valid.
        if count_permutations(half) < k:
            return ""

        half_length = sum(half)
        first_half = []

        for _ in range(half_length):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                cnt = count_permutations(half)

                if cnt >= k:
                    first_half.append(chr(i + ord("a")))
                    break
                else:
                    k -= cnt
                    half[i] += 1

        left = "".join(first_half)
        return left + middle + left[::-1]