class Solution:
    def candy(self, ratings) -> int:
        # think about base cases
        # if rating [0] > [1] then [0] need > [1]
        # if rating [0] <= [1] then [0] = 1
        # we can find the troughs (lte both neighbours) and assign as 1
        # for every neighbour of a "1" (as cur)
        # # cur <= other OR -> IF cur == trough then cur = 1 ELSE cur = 2
        # # cur > other -> IF other is set then cur = other + 1 ELSE ignore
        n = len(ratings)
        if n == 1:
            return 1
        # candies = [None] * n
        # #seed the troughs with 1s
        # #check last and first
        # def helper(i, check_i):
        #     #checks the neighbour (specified via check_i) of i
        #     j = i + check_i
        #     if j == -1 or j == n:
        #         return 
        #     if candies[j] != None:
        #         return
        #     if j + check_i == -1 or j + check_i == n or ratings[j] <= ratings[j + check_i]:
        #         if ratings[i] == ratings[j]:
        #             #this shldnt happen! this is a trough except recursion before for loop
        #             candies[j] = 1
        #         else:
        #             candies[j] = candies[i] + 1
        #         helper(j, check_i)
        #     elif candies[j + check_i] != None:
        #         candies[j] = candies[j + check_i] + 1

        # if ratings[0] <= ratings[1]:
        #     candies[0] = 1
        # if ratings[-1] <= ratings[-2]:
        #     candies[-1] = 1
        # for i in range(1, n - 1):
        #     if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
        #         candies[i] = 1
        #         helper(i, 1)
        #         helper(i, -1)

        # i = 0
        # c = 0
        # while None in candies:
        #     # 1 to n - 2
        #     if i != 0 and candies[i-1] == None:
        #         helper(i, -1)
        #     if i != n - 1 and candies[i+1] == None:
        #         helper(i, 1)
        #     i = (i + 1) % n
        #     c += 1
            
        # return sum(candies)

        #FAILED 
        #trying again after seeing double pass greedy solution

        #thoughts: i overthought this and thought it was a recursive thing stemming from the guaranteed base cases or the troughs
        #think more of invariants! and how to build via invariance to the solution
        #thus double pass soln is 2 for loops: START with all children getting 1 candy, then compare to left and if condition is met set as [i-1] + 1
        #above gives the invariance that problem is solved if only considering left neighbour
        #then for loop compare to right, get the MAX candy + 1 if condition is met.
        #adds the invariance that the problem is solved if considering right neighbour
        #basically a double prefix sum
        
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)

    
sol = Solution()
print(sol.candy([1,2,87,87,87,2,1]))
        
    