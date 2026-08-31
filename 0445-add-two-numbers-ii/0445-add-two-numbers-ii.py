class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []

        # Put digits into stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Add from right to left
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            # Insert new node at the beginning
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        return head