class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq= [] # creating the heap array

        for num in nums: # run until the num push the num in heap
            heappush(hq,num)
            if len(hq)>k: # if length of heap is greater than k then pop the heap value
                heappop(hq)

        return hq[0] # return the heap of 0th value