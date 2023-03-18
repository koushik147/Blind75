class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() # craeting a dummy node
        curr = dummy # assigning the curr to dummy node
        
        l1 = list1 # assigning the l1 to list1
        l2 = list2 # assigning the l2 to list2

        while l1 and l2: # run until l1 and l2
            if l1.val <= l2.val: # if l1 value is less than l2 value then assign l1 to current next
                curr.next = l1
                l1 = l1.next # assigning the next of l1

            else:
                curr.next = l2 # assigning curr pointer to l2
                l2 = l2.next # assigning the next of l2

            curr = curr.next # incrementing curr

        if l1 or l2: # if one of l1 or l2 gets over then append the excess array to curr
            if l1:
                curr.next = l1
            else:
                curr.next = l2
        
        return dummy.next # returning the dummy.next node