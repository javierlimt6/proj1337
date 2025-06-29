class Solution:
    def minWindow(self, s: str, t: str):
        from collections import Counter
        # #pre-process
        # idx_dict = {}
        # idx_list = []
        # l = None
        # r = None
        # #i need to get a count for the first substring
        # t_count = Counter(t)
        # restart_count = Counter("")
        # for char in t:
        #     restart_count[char] = 0
        # for i, char in enumerate(s):
        #     if char in t:
        #         if idx_dict == {}:
        #             l = i
        #         if t_count.most_common(1)[0][1] > 0:
        #             t_count[char] -= 1
        #             if t_count.most_common(1)[0][1] <= 0:
        #                 r = i
        #         idx_list.append((i, char))
        #         if char in idx_dict:
        #             idx_dict[char].append(i)
        #         else:
        #             idx_dict[char] = [i]
        # if l == None or r == None:
        #     return ""

        # cand = [l, r]
        # l_ptr, r_ptr = -1, -1
        # for i in range(len(idx_list)):
        #     if l == idx_list[i][0]:
        #         l_ptr = i
        #     if r == idx_list[i][0]:
        #         r_ptr = i
        # while r_ptr < len(idx_list):
        #     restart_count[idx_list[l_ptr][1]] -= 1 
        #     l_ptr += 1
        #     while restart_count[idx_list[l_ptr - 1][1]] < 0 and r_ptr < len(idx_list) - 1:
        #         r_ptr += 1
        #         restart_count[idx_list[r_ptr][1]] += 1
        #     if restart_count[idx_list[l_ptr - 1][1]] >= 0:
        #         if (idx_list[r_ptr][0] - idx_list[l_ptr][0]) < (cand[1] - cand[0]):
        #             cand = [idx_list[l_ptr][0], idx_list[r_ptr][0]]
        # return s[cand[0]: cand[1] + 1]
    
    #FAILED but close

        #second attempt after watching neetcode

        t_count = Counter(t)
        window_count = {}

        l = 0
        cand = []
        need = len(t_count)
        have = 0

        for r, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

                while l <= r and have == need:

                    if not cand or (r - l) < (cand[1] - cand[0]):
                        cand = [l, r]

                    window_count[s[l]] -= 1

                    if window_count[s[l]] < t_count[s[l]]:
                        have -= 1

                    l += 1

        
        if not cand:
            return ""
        
        return s[cand[0]: cand[1] + 1]

        #PASSED, good job

        



    
sol = Solution()
print(sol.minWindow("bba","ab"))

        