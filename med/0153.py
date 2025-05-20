def findMin(nums: List[int]) -> int:
    
    ## ok so we definitely need to be comparing the middle 
    ## check the 'slope' and determine where it is 
    # if low < high
    # return low
    # then
    # if mid > high 
    # mid = low + 1
    # else
    # mid = high - 1
    low = 0
    high = len(nums) - 1
    mid = low + (high - low) // 2
    while low < high:
        mid = low + (high - low) // 2
        if mid != 0 and mid != len(nums) - 1 and nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
            return nums[mid]
        else:
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return nums[low]


#passed
#comments on first attempt: alot of troubles with 1. validating whether the trough was found 2. whether to + 1 or not
#but ok ah did it! nubbad