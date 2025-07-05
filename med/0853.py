def carFleet(target: int, position, speed):
    #result is likely the size of the stack
# 10
# 8
# 0
# 5
# 3
#find the brute force soln
# while loop: add speed to pos, if pos got change then reduce speed + adjust pos
# we can merge them together using the stack?
# we can sort to determine whether the pos should merge or not
    # fleets = []
    # for i in range(len(position)):
    #     fleets.append([position[i], speed[i]])
    # fleets.sort(key = lambda x : x[0])
    # res = 0
    # while fleets:
    #     for i in range(len(fleets)):
    #         fleets[i][0] += fleets[i][1]
    #     j = -1
    #     while -j < len(fleets):
    #         if fleets[j][0] <= fleets[j-1][0]:
    #             fleets.pop(j-1)
    #         else:
    #             j -= 1
    #     while fleets and fleets[-1][0] >= target:
    #         fleets.pop()
    #         res += 1
    # return res

    #FAILED 

    fleets = sorted(zip(position, speed))
    time_to_target = [float(target - p) / s for p, s in fleets]
    res = 0
    while len(time_to_target) > 1:
        front = time_to_target.pop()
        if front < time_to_target[-1]:
            res += 1
        else:
            time_to_target[-1] = front
    return res + len(time_to_target)

    #PASSED
    #after reading solution
    #no need to simulate EVERY time step
    # we can just calculate arrival times directly
    # cause we really only need to compare the one car in front
    # the first car cannot overtake the last car without going past the second car
    # so we can just abstract the logic to the neighbouring cars
    # thus can calculate arrival times
    # step granularity issues too