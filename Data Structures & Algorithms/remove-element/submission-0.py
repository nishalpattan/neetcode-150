class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_ptr = 0
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != val:
                nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                write_ptr += 1
        return write_ptr