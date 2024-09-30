class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c0 = 0
        c = 0
        first = True
        if 1 not in flowerbed:
            c = (len(flowerbed) + 1) // 2
            if c >= n:
                return True
            else:
                return False
        for i, plot in enumerate(flowerbed):
            if (plot == 1): # at 1
                if first and (c0 > 1): #at first 1
                    c += c0//2
                elif (c0 > 2): #not first
                    c += (((c0 + 1) //2) - 1)
                first = False
                c0 = 0
            elif (i == (len(flowerbed) - 1)) and (c0 >= 1): # at 0 end
                c += (c0 + 1)//2
                c0 = 0
            else: #at 0 continue
                c0 += 1
        if c >= n:
            return True
        else:
            return False
