class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
        Do not return anything, modify head in-place instead.
        """
    
        #calling the find mid function 
        mid=self.findMid(head)
        #assigning the midnext value to null 
        midNext=mid.next
        mid.next=None
        
        #for reversing head is the next element of mid
        headB=self.reverse(midNext)
        
        #we dont want to loose the head
        headA=head
        self.mergelinkedlist(headA,headB)
         
    def findMid(self,head):
        #two pointers way to find the mid
        slow=head
        fast=head
        #until fast is null in odd case and next.next in even 
        while fast.next and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            #return the slow pointer which is at mid now
        return slow  
        
    def reverse(self,head):
        #template for reverse linked list
        prev=None
        curr=head
        #carryout until curr is none
        while curr !=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            #return the prev pointer which will giove the reversed list
        return prev 
        
        
    def mergelinkedlist(self,head1,head2):
        #assigning the head values 
        p1=head1
        p2=head2
        #until the p2 is null iterate through the linked list
        while p2:
            #temp is next of p1
            temp=p1.next
            #p2 is next of p1
            p1.next=p2
            #move the list p2 by one
            p2=p2.next
            #p1's next of next is temp
            p1.next.next=temp
            
            p1=temp 