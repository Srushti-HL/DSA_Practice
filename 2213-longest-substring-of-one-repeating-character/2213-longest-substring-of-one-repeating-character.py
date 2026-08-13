class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.s = list(s)
        self.build(1, 0, self.n - 1)

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        lchar, rchar, lpref, lsuff, lmax, llen = left
        l2char, r2char, rpref, rsuff, rmax, rlen = right

        prefix = lpref
        if lpref == llen and lchar == l2char:
            prefix = llen + rpref

        suffix = rsuff
        if rsuff == rlen and rchar == r2char:
            suffix = rlen + lsuff

        maximum = max(lmax, rmax)

        if rchar == l2char:
            maximum = max(maximum, lsuff + rpref)

        return (
            lchar,
            r2char,
            prefix,
            suffix,
            maximum,
            llen + rlen
        )

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = (
                self.s[start],
                self.s[start],
                1,
                1,
                1,
                1
            )
            return

        mid = (start + end) // 2

        self.build(node * 2, start, mid)
        self.build(node * 2 + 1, mid + 1, end)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(self, node, start, end, index, char):
        if start == end:
            self.tree[node] = (
                char,
                char,
                1,
                1,
                1,
                1
            )
            return

        mid = (start + end) // 2

        if index <= mid:
            self.update(node * 2, start, mid, index, char)
        else:
            self.update(node * 2 + 1, mid + 1, end, index, char)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def change(self, index, char):
        self.update(1, 0, self.n - 1, index, char)

    def get_max(self):
        return self.tree[1][4]


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int]
    ) -> list[int]:

        tree = SegmentTree(s)
        result = []

        for char, index in zip(queryCharacters, queryIndices):
            tree.change(index, char)
            result.append(tree.get_max())

        return result