class Solution:
    def primeSubarray(nums, k):
        #use 2 pointers and move around, storing the max and min prime number, updating
        def check(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        prime_list = []
        for i, n in enumerate(nums):
            if check(n):
                prime_list.append([i, n])
        
        #do some prefix
        i = 0
        j = 1
        c = 0
        high = max(prime_list[0][1], prime_list[1][1])
        low = min(prime_list[0][1], prime_list[1][1])
        print(high, low, prime_list)
        while i != len(prime_list) - 1 and j != len(prime_list):
            if i == j:
                j += 1
                #update
                if j != len(prime_list):
                    high = max(high, prime_list[j][1])
                    low = min(low, prime_list[j][1])
            elif high - low <= k:
                c += prime_list[j][0] - prime_list[i][0]
                j += 1
                #update
                if j != len(prime_list):
                    high = max(high, prime_list[j][1])
                    low = min(low, prime_list[j][1])
            else:
                if prime_list[i][1] == high:
                    high = -1
                    for l in range(i + 1,j + 1):
                        high = max(high, prime_list[l][1])
                if prime_list[i][1] == low:
                    low = 9999999999
                    for l in range(i + 1,j + 1):
                        low = min(low, prime_list[l][1])
                i += 1

        return c
    

print(Solution.primeSubarray([2,3,5,7], 3))