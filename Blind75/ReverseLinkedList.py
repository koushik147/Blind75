class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #assigning a previous node  before head
        prev=None
        #changing the head node to current
        curr=head
        #iterate until the current is none
        while curr:
            #temperory variable is after the current node
            temp=curr.next
            #assigning the next current value to previous
            curr.next=prev
            #move the previous node to next ie: current
            prev=curr
            #move the current to next node ie:temp
            curr=temp
         #return the previous as the head   
        return prev