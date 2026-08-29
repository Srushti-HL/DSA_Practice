class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        start = 0

        for i in range(1, n + 1):
            # End of a connected group
            if i == n or arr[i][0] - arr[i - 1][0] > limit:

                # Values in this group are already sorted
                values = [arr[j][0] for j in range(start, i)]

                # Get their original indices and sort them
                indices = sorted(arr[j][1] for j in range(start, i))

                # Put smallest value at smallest index
                for idx, value in zip(indices, values):
                    ans[idx] = value

                start = i

        return ans