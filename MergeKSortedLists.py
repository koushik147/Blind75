#Time_Complexity: O(nlogk)
#Space_Complexity: O(n)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        ListNode.__lt__ = lambda a,b : a.val<b.val # creating the custom comparator by overrding the default lessthan operator by defining the __lt__ function with lambda function
        minheap=[] # creating the minheap
            
        result = ListNode(-1) # defining the dummy node
        curr = result # assigning the result to current

        for lhead in lists: # run until head in lists if head present then push that to heap array
            if lhead:
                heappush(minheap,lhead)

        while minheap: # run until the minheap is not null
            top = heappop(minheap) # pop the heap value and store in top
            curr.next = top # assigning the top to curr.next
            curr = curr.next # assign the curr to curr.next
            if top.next: # if top.next is not null
                heappush(minheap,top.next) # push the top.next value in the heap array


        return result.next # return the result.next value
            
