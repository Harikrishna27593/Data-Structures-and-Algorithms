import sys

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        if k>=3:
            nums2=list(set(nums))
            nums2.sort()
            if len(nums2)>=3:
                return nums2[len(nums2)-3]
            elif len(nums2)==2:
                return max(nums2)
            else :
                return max(nums2)
                
        else:
            return max(nums)