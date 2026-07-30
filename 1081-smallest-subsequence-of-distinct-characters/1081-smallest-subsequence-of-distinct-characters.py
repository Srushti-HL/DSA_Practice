class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {}

        # Store the last occurrence of each character
        for i, ch in enumerate(s):
            last_index[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            # Skip if already included
            if ch in seen:
                continue

            # Make the result lexicographically smaller
            while (stack and
                   ch < stack[-1] and
                   last_index[stack[-1]] > i):

                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)