from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append([l, r, w, i])

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next_idx[i] = first interval that starts AFTER arr[i]'s end
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        # dp(i, k) returns:
        # (maximum weight, lexicographically smallest indices)
        memo = {}

        def dp(i, k):
            if i >= n or k == 0:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]

            # Option 1: skip current interval
            skip_score, skip_indices = dp(i + 1, k)

            # Option 2: take current interval
            take_score, take_indices = dp(next_idx[i], k - 1)

            take_score += arr[i][2]
            take_indices = tuple(sorted(
                take_indices + (arr[i][3],)
            ))

            # Choose the better option
            if take_score > skip_score:
                result = (take_score, take_indices)
            elif take_score < skip_score:
                result = (skip_score, skip_indices)
            else:
                # Same score → lexicographically smaller indices
                result = min(
                    (take_score, take_indices),
                    (skip_score, skip_indices),
                    key=lambda x: x[1]
                )

            memo[(i, k)] = result
            return result

        return list(dp(0, 4)[1])