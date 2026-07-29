class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(start, path):
            # If we have chosen k numbers, store the combination
            if len(path) == k:
                result.append(path[:])
                return

            # Try all possible numbers from 'start' to n
            for i in range(start, n + 1):
                path.append(i)          # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()              # Backtrack

        backtrack(1, [])
        return result