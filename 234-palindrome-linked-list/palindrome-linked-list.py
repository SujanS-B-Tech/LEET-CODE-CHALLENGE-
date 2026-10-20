# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        ans = []
        curr = head

        while curr != None:
            ans.append(curr.val)
            curr = curr.next
        return ans == ans[::-1]