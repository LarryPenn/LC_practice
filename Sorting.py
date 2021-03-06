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
                

//34. Find First and Last Position of Element in Sorted Array
//https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        low = 0
        high = len(nums)-1
        mid = int((low+high)/2)
        res = -1
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        
        while low < high :
            if nums[mid] > target:
                high = mid
                mid = int((low+high)/2)
            elif nums[mid] < target:
                low = mid + 1
                mid = int((low+high)/2) 
            else:
                i = 0
                while mid - i >=0 and nums[mid-i] == target:
                    i += 1
                j = 0
                while mid + j < len(nums) and nums[mid + j] == target:
                    j += 1
                return [mid - i + 1, mid + j -1]
            
        if low == high and nums[low] == target:
            return [low, high]
        
        return [-1, -1]
            
                
//https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        if len(intervals) < 2:
            return intervals
        
        i = 0
        
        while i + 1 < len(intervals):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i+1][1], intervals[i][1])]
                intervals.pop(i)
                print(i)
                i = i - 1
            i += 1
        
        return intervals


https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def searchPivot(nums):
            lo = 0
            hi = len(nums) - 1
            mid = (lo + hi) // 2
            
            while lo < hi:
                if nums[mid + 1] < nums[mid]:
                    return mid + 1
                if nums[mid] > nums[hi]:
                    lo = mid
                    mid = (lo + hi) // 2
                else:
                    hi = mid
                    mid = (lo + hi) // 2
            
            return 0 
                
        
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
            
        pivot = searchPivot(nums)
        print(pivot)
        
        arr = nums[pivot:]
        if pivot > 0:
            arr += nums[:pivot]
        
        #print(arr)
        
        lo = 0
        hi = len(arr)-1
        mid = (lo + hi) // 2
        #print(lo, mid, hi)
        
        while lo <= hi:
            print(arr[mid], target)
            if arr[mid] == target:
                return (mid + pivot)%len(arr)
            elif arr[mid] < target:
                lo = mid + 1
                mid = (lo + hi) //2
                
            else:
                hi = mid - 1
                mid = (lo + hi) //2
                
        return -1
        
        
 //https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/805/   
        
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort the array based on finish time
        # iterate from left to right and add to existing room if no conflict, and create a new room if there is a conflict. Use a dictionary to store room number (key), meeting (value) pairs
        
        def intersect(range1, range2):
            if range1[0] < range2[0] and range1[1] <= range2[0]:
                return False
            if range1[0] >= range2[1] and range1[0] > range2[0]:
                return False
            return True
        
        
        print(intersect([0,30], [5, 10]))
        intervals.sort(key = lambda x:x[0])
        
        rooms = {}
        
        for interval in intervals:
            if not rooms:
                rooms['1'] = [interval]
            else: 
                inserted = False
                for key in rooms:
                    flag = False
                    for timeslot in rooms[key]:
                        if intersect(timeslot, interval):
                            flag = True
                    if not flag:
                        rooms[key].append(interval)
                        inserted = True
                        break;
                if not inserted:
                    rooms[len(rooms.keys()) + 1] = [interval]

        print(rooms)
        
        return len(rooms.keys())

https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def binarySearch(arr, target):
            lo = 0
            hi = len(arr) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if target == arr[mid]:
                    return True
                elif target < arr[mid]:
                    hi = mid - 1
                else: 
                    lo = mid + 1
            
            return False
        
        
        result = False
        for array in matrix:
            if len(array) == 0:
                continue
            if array[0] <= target and array[-1] >= target:
                if binarySearch(array, target):
                    result = True
                    break
        
        return result
        
        