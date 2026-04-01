class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, start = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[start] = nums[start], nums[i]
                    start += 1
            nums[start], nums[r] = nums[r], nums[start]
            pivot_index = start
            if pivot_index < k:
                return quickSelect(pivot_index + 1, r)
            elif pivot_index > k:
                return quickSelect(l, pivot_index-1)
            else:
                return nums[k]

        return quickSelect(0, len(nums)-1)