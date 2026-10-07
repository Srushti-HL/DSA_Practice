class Solution:
    def finalValueAfterOperations(self, operations):
        X = 0

        for operation in operations:
            if '+' in operation:
                X += 1
            else:
                X -= 1

        return X