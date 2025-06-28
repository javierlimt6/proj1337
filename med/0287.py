class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duped = [False] * (len(nums) - 1)
        for i in nums:
            if duped[i - 1]:
                return i
            else:
                duped[i - 1] = True
        
#PASSED
#simple but i wonder about the linked list solution