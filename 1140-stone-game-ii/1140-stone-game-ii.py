class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def solve(i, M):
            # All remaining piles can be taken
            if 2 * M >= n - i:
                return suffix[i]

            # Already calculated
            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                opponent = solve(i + X, max(M, X))

                # Total remaining - opponent's maximum
                current_player = suffix[i] - opponent

                best = max(best, current_player)

            memo[(i, M)] = best
            return best

        return solve(0, 1)