class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1 # handling edge case
        
        if len(nums)>1 and nums[0] > nums[1]: return 0

		# calculate mid
        left = 0
        right = len(nums) - 1
		#traverse through the elements using binary search
        while left < right:
            mid = left + (right - left) // 2 
            if nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1 
        return left