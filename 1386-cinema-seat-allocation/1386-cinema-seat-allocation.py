class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Every row can initially fit 2 groups
        ans = 2 * n

        for seats in rows.values():

            # This row was counted as 2 groups.
            # Recalculate based on its reserved seats.
            groups = 0

            # Left block: 2,3,4,5
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # Middle block: 4,5,6,7
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # Right block: 6,7,8,9
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                groups = 2
            elif left or middle or right:
                groups = 1

            # Replace the initial 2 groups for this row
            ans -= 2
            ans += groups

        return ans