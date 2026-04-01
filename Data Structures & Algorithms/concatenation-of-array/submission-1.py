class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for idx in range(n):
            ans[idx] = nums[idx]
            ans[idx + n] = nums[idx]
        return ans
