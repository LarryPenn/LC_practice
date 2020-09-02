//https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p0 = i = 0
        p2 = len(nums) - 1
        while i<= p2:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[p0]
                nums[p0] = temp
                p0 += 1
                i += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[p2]
                nums[p2] = temp
                p2 -= 1
            else:
                i += 1
        
        
        