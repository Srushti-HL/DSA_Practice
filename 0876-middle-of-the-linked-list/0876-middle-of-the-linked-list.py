# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head
        len=0
        while(head!=None):
            len=len+1
            head=head.next
        len=len//2
        len=len+1
        head=l
        count=0
        while(head!=None):
            count+=1
            if count is len:
                return head
            head=head.next
        