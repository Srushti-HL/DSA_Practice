class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def dfs(i, j):
            if i == j:
                return nums[i]

            if (i, j) in memo:
                return memo[(i, j)]

            left = nums[i] - dfs(i + 1, j)
            right = nums[j] - dfs(i, j - 1)

            memo[(i, j)] = max(left, right)
            return memo[(i, j)]

        return dfs(0, n - 1) >= 0