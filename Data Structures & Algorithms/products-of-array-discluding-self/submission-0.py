class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach 1: Two array based approach
        # Time complexity : O(n)
        # space complexity : O(n + n)
        left_array = [1 for _ in range(len(nums))]
        right_array = [1 for _ in range(len(nums))]
        res = list()

        for idx in range(1, len(nums)):
            left_array[idx] = left_array[idx-1] * nums[idx-1]
        
        for idx in range(len(nums)-2, -1, -1):
            right_array[idx] = right_array[idx+1] * nums[idx+1]
        
        for idx in range(len(nums)):
            res.append(left_array[idx] * right_array[idx])
        
        return res