class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute Force solution: loop through the nums array twice and 
        check if the sum matches to the target
         TC O(n ^ 2), SC : O(1)
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]
        return []
        