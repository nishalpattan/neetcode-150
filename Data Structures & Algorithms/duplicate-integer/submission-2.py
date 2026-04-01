class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         ''' naive solution
         TC : O(n logn)
         SC : O(1)
         if len(nums) == 1 or len(nums) == 0:
            return False
         nums.sort()
         for idx, val in enumerate(nums):
            if idx != 0:
                if nums[idx] == nums[idx-1]:
                    return True
         return False
         '''
         # efficient solution using hashmaps
         # TC : O(n), SC : O(n)
         hashMap = dict()
         for val in nums:
            if val in hashMap:
                hashMap[val] += 1
            else:
                hashMap[val] = 1
         for val in nums:
            if hashMap[val] > 1:
                return True
         return False

