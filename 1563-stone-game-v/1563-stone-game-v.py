from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):

        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(i, j):
            if i >= j:
                return 0

            ans = 0

            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):

                left += stoneValue[k]
                right -= stoneValue[k]

                # Left side is smaller
                if left < right:

                    # Even the current left side cannot
                    # improve the answer.
                    if ans >= left * 2:
                        continue

                    ans = max(
                        ans,
                        left + dfs(i, k)
                    )

                # Right side is smaller
                elif left > right:

                    # Since right will only decrease from here,
                    # if current right cannot improve answer,
                    # later splits cannot improve it either.
                    if ans >= right * 2:
                        break

                    ans = max(
                        ans,
                        right + dfs(k + 1, j)
                    )

                # Equal
                else:
                    ans = max(
                        ans,
                        left + dfs(i, k),
                        right + dfs(k + 1, j)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)