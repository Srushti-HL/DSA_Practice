class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(index, subset):
            if index == len(nums):
                res.append(subset[:])
                return

            # Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Exclude nums[index]
            subset.pop()
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res