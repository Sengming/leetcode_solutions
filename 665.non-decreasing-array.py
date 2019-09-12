class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
                return True

        cnt = 0
        #now we have len > 3
        for i in range(len(nums)-1):
                if nums[i] <= nums[i+1]:
                        continue
                else:
                        cnt+=1

        if cnt <= 1:
                return True
        else:
                return False
        
