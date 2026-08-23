class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        q_diff = right_q - left_q
        sum_diff = left_sum - right_sum

        # Odd number of unmatched '?' → Alice wins
        if q_diff % 2 != 0:
            return True

        # Bob wins only if the sums can be perfectly balanced
        return sum_diff != 9 * q_diff // 2