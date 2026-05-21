class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for idx in range(len(nums) - 2):
            if idx >0 and nums[idx] == nums[idx-1]:
                continue
            start = idx + 1
            end = len(nums) - 1
            while start < end:
                curr_sum = nums[idx] + nums[start] + nums[end]
                if curr_sum == 0:
                    res.append([nums[idx], nums[start], nums[end]])
                    while start < len(nums) - 1 and nums[start] == nums[start+1]:
                        start += 1
                    while end > 0 and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif curr_sum > 0:
                    end -= 1
                else:
                    start += 1

        return res