def maxKelements(nums, k):
    import heapq
    import math
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)
    score = 0

    for _ in range(k):
        m = -heapq.heappop(max_heap)
        score += m
        heapq.heappush(max_heap, -(math.ceil(m / 3)))

    return score
