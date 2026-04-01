import sys
sys.setrecursionlimit(3000) 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # solve using quick sort as it will sort the array with O(n logn) time complexity
        # and without using extra space to store the result other than recursive call stack

        # using lomuto partition to pick the first element as pivot and moving it to the right position

        def quick_sort(nums, start, end):
            if start < end:
                pivot_idx = partition(nums, start, end)
                quick_sort(nums, start, pivot_idx-1)
                quick_sort(nums, pivot_idx + 1, end)
        
        def partition(nums, start, end):
            pivot = nums[end]
            write_ptr = start-1
            for read_ptr in range(start, end):
                if nums[read_ptr] <= pivot:
                    write_ptr += 1
                    nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
            nums[end], nums[write_ptr+1] = nums[write_ptr+1], nums[end]
            return write_ptr+1
        
        quick_sort(nums, 0, len(nums)-1)
        return nums