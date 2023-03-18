#TC: O(n) 
#SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initializing the count variable
        count=0
        #initializing a  dummy variable
        dummy=ListNode(0,head)
        
        #ititializing the slow and fast to dummy
        slow=dummy
        fast=dummy
        
        #logic
        while count<n:

            #increment the fast pointer by one until it reached count value
            fast=fast.next
            count+=1
            #if count value is reached then move both pointers
        while fast.next!=None:
            #move both the fast and slow pointers by one now
            slow=slow.next
            fast=fast.next
        #logic to delete the n th element 
        slow.next=slow.next.next
        
        #return the dummy variable now 
        return dummy.next
        
