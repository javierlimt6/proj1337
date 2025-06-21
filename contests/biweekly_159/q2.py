class Solution:
    def maxArea(coords) -> int:
        x_dict = {}
        y_dict = {}
        x_coord = map(lambda x:x[0], coords)
        y_coord = map(lambda y:y[1], coords)
        for c in coords:
            if c[0] not in x_dict:
                x_dict[c[0]] = [c]
            else:
                x_dict[c[0]].append(c)
            if c[1] not in y_dict:
                y_dict[c[1]] = [c]
            else:
                y_dict[c[1]].append(c)

        contest = -1
        high_x = max(x_dict.keys())
        high_y = max(y_dict.keys())
        low_x = min(x_dict.keys())
        low_y = min(y_dict.keys())
        print(x_dict, y_dict)
        for key, coords in x_dict.items():
            if len(coords) > 1:
                # import pdb; pdb.set_trace()
                
                y = list(map(lambda c: c[1], coords))
                line_length = max(y) - min(y)
                compare = list(map(lambda x: abs(key - x), x_dict.keys()))
                max_h = max(abs(high_x - key), abs(low_x - key))
                print(key, y, line_length, max_h, compare, list(x_coord))
                contest = max(contest, line_length * max_h)

        for key, coords in y_dict.items():
            if len(coords) > 1:
                x = list(map(lambda c: c[0], coords))
                line_length = max(x) - min(x)
                max_h = max(list(map(lambda y: abs(key - y), list(y_coord).copy())), default = 0)
                contest = max(contest, line_length * max_h)

        if contest <= 0:
            return -1
        
        return contest

print(Solution.maxArea([[1,7],[1,8],[10,2],[8,1],[8,10]]
))