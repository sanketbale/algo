# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # start traversing
        node = head
        head2 = ListNode()

        ptr = ListNode()

        if (node is not None and node.next is not None):
            ptr.val = head.val
            node = node.next
        else:
            return head

        while (node is not None):
            temp = ListNode()
            temp.val = node.val
            temp.next = ptr

            head2.val = node.val
            head2.next = ptr

            ptr = temp
            node = node.next

        return head2