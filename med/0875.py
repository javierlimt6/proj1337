def minEatingSpeed(piles, h: int) -> int:
    #assume len(piles) <= h
    import math
    def valid(k):
        c = 0
        for p in piles:
            c += math.ceil(p / k)
        return c <= h
    lowest = 1
    highest = max(piles)
    k = (lowest + highest) // 2
    while highest > lowest:
        if valid(k):
            highest = k
            k = (lowest + highest) // 2
        else:
            lowest = k + 1 
            k = (lowest + highest) // 2
    return k