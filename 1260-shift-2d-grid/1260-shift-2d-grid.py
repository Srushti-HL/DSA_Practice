class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        total = m * n
        k %= total

        # Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)

        # Shift
        arr = arr[-k:] + arr[:-k] if k else arr

        # Convert back to 2D grid
        answer = []
        index = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[index])
                index += 1
            answer.append(row)

        return answer