class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.middle(head)
        right = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)

    def middle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while h1 and h2:
            if h1.val <= h2.val:
                current.next = h1
                h1 = h1.next
            else:
                current.next = h2
                h2 = h2.next
            current = current.next

        current.next = h1 if h1 else h2
        return dummy.next