class Solution:
    def search(self, nums, target):
        #invariance: either low to mid or mid to high is sorted
        #if mid > low then strictly incr
        #if mid > high then 
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[high] == target:
                return high
            if nums[low] == target:
                return low
            if nums[mid] < nums[high]:
                #if right side sorted
                if nums[mid] < target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                #left side sorted
                if nums[low] < target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
    
    #PASSED after hint of finding which part is sorted
