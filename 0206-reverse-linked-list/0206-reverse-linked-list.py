class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # 1. Save next node
            curr.next = prev        # 2. Reverse the pointer
            prev = curr             # 3. Move prev
            curr = next_node        # 4. Move curr

        return prev