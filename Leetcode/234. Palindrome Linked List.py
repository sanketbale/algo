# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         node = head
#         isPalindrom = True
#         # get all elements in array by traversing linked list
#         temp = []
#         while (node is not None):
#             temp.append(node.val)
#             node = node.next
#
#         # pop from array and check again by traversing the array
#         node = head
#         i = len(temp) - 1
#         while (node is not None and isPalindrom):
#             if (node.val != temp[i]):
#                 isPalindrom = False
#             i = i - 1
#             node = node.next
#
#         return isPalindrom


import math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        isPalindrom = True
        mid = ListNode()
        ptr2 = ListNode()
        ptr3 = ListNode()
        # get all elements in array by traversing linked list
        size = 0
        while (node is not None):
            node = node.next
            size = size + 1

            # start again
        node = head
        countr = 0
        while (node is not None):

            if (countr == math.ceil(size / 2)):
                ptr2.val = node.val
                mid = node
                ptr3.val = node.val

            if (countr > math.ceil(size / 2)):
                temp = ListNode()
                temp.val = node.val
                temp.next = ptr2
                ptr3.val = node.val
                ptr3.next = ptr2
                ptr2 = temp

            node = node.next
            countr = countr + 1

            # traverse again
        node = head
        countr = 0
        while (node is not None and isPalindrom and countr < math.floor(size / 2)):
            print (node.val)
            print (ptr3.val)
            isPalindrom = ptr3.val == node.val

            node = node.next
            ptr3 = ptr3.next

            countr = countr + 1

        return isPalindrom