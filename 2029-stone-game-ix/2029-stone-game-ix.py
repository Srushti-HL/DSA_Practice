class Solution:
    def stoneGameIX(self, stones):
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        def check(c):
            # Alice must start with a remainder-1 stone
            if c[1] == 0:
                return False

            c[1] -= 1

            # Number of alternating 1 and 2 moves
            turns = 1 + min(c[1], c[2]) * 2 + c[0]

            # If extra remainder-1 stones exist
            if c[1] > c[2]:
                c[1] -= 1
                turns += 1

            return turns % 2 == 1 and c[1] != c[2]

        # Try Alice starting with remainder 1
        option1 = check(count.copy())

        # Try Alice starting with remainder 2
        swapped = [count[0], count[2], count[1]]
        option2 = check(swapped)

        return option1 or option2