class Solution:
    @staticmethod
    def threeSum(nums):
        #predprocess in O(n), map each integer for O(1) retrieval
        #this gives O(n^2) 
        #or we can turn this into a 2sum problem
        #
        # int_idx = {}
        # for i, x in enumerate(nums):
        #     if x not in int_idx:
        #         int_idx[x] = [i]
        #     else:
        #         int_idx[x].append(i)
        # #-x becomes the "target"
        # #but how do we account for multiple targets?
        # #used 1 prompt
        # #sort first, then have the 2 pointers increment from front and back
        # #nvm i think best is O(n^2)
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         two_sum = nums[i] + nums[j]
        #         if (-two_sum) in int_idx:
        #             #validation check, make sure not using dupes
        #             #if there is an index in int_idx that is not i or j
        #             for k in int_idx[-two_sum]:
        #                 if k != i and k != j:
        #                     res.add(sorted([nums[i],nums[j],nums[k]]))
        #                     break
        #ok failed time complexity due to this for loop
        #trying sorting + 2 pointer soln
  
        #O(n^2) space O(n) or O(1)
        nums.sort()
        res = set()
        for n in range(len(nums)):
            if nums[n] > 0:
                break
            l = n + 1
            r = len(nums) - 1
            while r > l:
                if nums[l] + nums[r] + nums[n] == 0:
                    res.add((nums[n], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] + nums[n] > 0:
                    r -= 1
                else:
                    l += 1
        return list(res)
        #finally solved it
        #alot of errors, very badly done
        #note the auto handling of the duplicates, very important


        
print(Solution.threeSum([-1,0,1,2,-1,-4]))