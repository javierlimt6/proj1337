class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        even_c = 0
        odd_c = 0
        simp = []
        for el in nums:
            if el % 2 == 0:
                even_c += 1
                simp.append(0)
            elif el % 2 == 1:
                odd_c += 1
                simp.append(1)
        
        

        if abs(even_c - odd_c) > 1:
            return -1
        
