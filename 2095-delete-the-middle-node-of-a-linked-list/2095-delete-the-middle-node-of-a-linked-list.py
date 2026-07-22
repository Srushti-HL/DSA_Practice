# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        arr = []

        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        # If there is only one node.
        if len(arr) == 1:
            return None

        # Delete the middle element.
        mid = len(arr) // 2
        arr.pop(mid)

        # Create the new linked list.
        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next