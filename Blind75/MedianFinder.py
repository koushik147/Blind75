class MedianFinder(object):

    def __init__(self):
       self.first_max = []
       self.sec_min = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # add the element into max heap
        # pivot is the max of max heap - compare num with pivot
        # if num > pivot , add that to second_min heap
        if self.first_max and -self.first_max[0] < num:
            heappush(self.sec_min,num)

        else:
            heappush(self.first_max,-num)

        # if len(first_max) > len(sec_min) +1, then heappop(first_max) and add it in sec_min
        if len(self.first_max) > len(self.sec_min) +1:
            val = -1 * heappop(self.first_max)
            heappush(self.sec_min,val)

        # if len(sec_min) > len(first_max) +1, then heappop(sec_min) and add it in first_max
        if len(self.sec_min) > len(self.first_max) +1:
            val = heappop(self.sec_min)
            heappush(self.first_max,-val)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.first_max) > len(self.sec_min): # if firstmax is greater than second min return the max heap by negate it
            return -self.first_max[0]

        if len(self.first_max) < len(self.sec_min): # if firstmax is lesser than second min
            return self.sec_min[0]

        return ((-self.first_max[0]) + self.sec_min[0])/2.0 # returning the median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()