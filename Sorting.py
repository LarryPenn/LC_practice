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
        
        

//https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        result = []
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
        for i in range (0, k):
            max = 0
            res = None
            for key in d.keys():
                if d[key] > max:
                    res = key
                    max = d[key]
        
            result.append(res)
            d.pop(res)
            
        return result
                