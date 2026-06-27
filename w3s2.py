# from collections import deque
# def blueprint_approval(blueprints):
#     # return sorted(blueprints)
#     q = deque(sorted(blueprints))
#     approved = []

#     while q:
#         approved.append(q.popleft())
#     return approved


# print(blueprint_approval([3, 5, 2, 1, 4]))
# print(blueprint_approval([7, 4, 6, 2, 5]))


# def build_skyscrapers(floors):
#     # input: integer array represnting floors
#     # output: num of skyscrapers

#     count = 1


#     for i in range(1,len(floors)):
#         if floors[i] > floors[i - 1]:
#             count +=1
#     return count
# print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))
# print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))
# print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))
def max_corridor_area(segments):
    l, r = 0 ,len(segments)
    runningMaxArea = 0

    while r > l:
        width = r - l + 1
        diff = segments[r] - segments[l]
        currArea = width * diff
        if currArea > runningMaxArea:

    # for i in range(len(segments)):

    #     for j in range(i +1, len(segments)):

    #         currArea = abs(j - i) * min(segments[i], segments[j])


    #         runningMaxArea = max(currArea, runningMaxArea)
    # return runningMaxArea
print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_corridor_area([1, 1]))
