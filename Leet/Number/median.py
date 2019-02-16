class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #nums1 = nums01
        #nums2 = nums02
        while True:
            #print nums1
            #print nums2
            if len(nums1) + len(nums2) <= 2 or not nums1 or not nums2:
                #print "OUT", nums1 + nums2
                return self.med(nums1 + nums2)

            if self.med(nums1) == self.med(nums2):
                return self.med(nums1)

            if self.med(nums1) < self.med(nums2):
                nums1 = nums1[len(nums1)/2:]
                nums2 = nums2[:(len(nums2)+1)/2]
            else:
                nums2 = nums2[len(nums2)/2:]
                nums1 = nums1[:(len(nums1)+1)/2]
        
        #print "DONE"
        
    def med(self, nums):
        if not nums:
            return 0
        sz = len(nums)
        ans = (nums[(sz-1)/2] + nums[sz/2])/2.0
        #print ans
        if float(int(ans)) == ans:
            return int(ans)
        return ans
        
