class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #two pointer approach
        slow=head
        fast=head
        # initially cycle is assigned to false
        cycle=False
        
        #iterate through the loop until fast pointer gets to null
        while fast!=None and fast.next!=None:
            slow=slow.next
            #moves two jumps
            fast=fast.next.next
            
            #if the slow matches to fast then change cycle variable to true
            if slow==fast:
                cycle=True
                #when cycle is detected break it
                break
                
                
        #if cycle is not there return null    
        if not cycle:
            return None
        #assign slow as head
        slow=head
        
        #iterate until the fast and slow meets
        while slow!=fast:
            slow=slow.next
            #then move both pointer by one node
            fast=fast.next
        #return either fast or slow pointer as it is same
        return fast