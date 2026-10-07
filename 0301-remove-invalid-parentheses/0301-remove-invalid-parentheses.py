class Solution:
    def removeInvalidParentheses(self, s):
        # Find minimum number of removals needed
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        def dfs(index, left, right, current):
            # No more removals needed
            if left == 0 and right == 0:
                remaining = ''.join(current[index:])

                candidate = ''.join(current) + remaining

                if is_valid(candidate):
                    result.add(candidate)

                return

            if index >= len(s):
                return

            ch = s[index]

            # Remove current '('
            if ch == '(' and left > 0:
                dfs(index + 1, left - 1, right, current)

            # Remove current ')'
            if ch == ')' and right > 0:
                dfs(index + 1, left, right - 1, current)

            # Keep current character
            current.append(ch)
            dfs(index + 1, left, right, current)
            current.pop()

        # Simpler DFS implementation
        result.clear()

        def backtrack(index, left, right, path):
            if index == len(s):
                if left == 0 and right == 0:
                    candidate = ''.join(path)

                    if is_valid(candidate):
                        result.add(candidate)
                return

            ch = s[index]

            # Remove '('
            if ch == '(' and left > 0:
                backtrack(index + 1, left - 1, right, path)

            # Remove ')'
            if ch == ')' and right > 0:
                backtrack(index + 1, left, right - 1, path)

            # Keep character
            path.append(ch)
            backtrack(index + 1, left, right, path)
            path.pop()

        backtrack(0, left_remove, right_remove, [])

        return list(result)