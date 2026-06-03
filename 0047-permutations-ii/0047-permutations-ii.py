class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                visited[i] = False

        backtrack([])
        return result