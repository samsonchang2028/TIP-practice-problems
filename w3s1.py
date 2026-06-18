"""
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on a set of instructions.

The instructions are provided as a 0-indexed string arrival_pattern of length n, consisting of the characters:

'I' - The next guest should have a higher number than the previous guest.
'D' - The next guest should have a lower number than the previous guest.
You need to create a string guest_order of length n + 1 that satisfies the following conditions:

guest_order contains each number from 1 to str(n + 1) exactly once. These numbers represent the guests' assigned numbers.
For every index i from 0 to n - 1:
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Among all valid orders, return the lexicographically smallest one.
"""

def arrange_guest_arrival_order(arrival_pattern):
    length = len(arrival_pattern) + 1
    stack = []
    res= []

    #input: a string of letters represneting the order of which theguests arrival_pattern
    #if I, the guest should be larger than the prev
    #if D, the guest num sohuld be less than the prev

    #output: an output string of nums that correspond to the order in whcih guests arrive


    # when we pop off the stack into res itll be in descending order -> "D"
    for i in range(length):
        stack.append(i + 1)

        if i == length -1 or arrival_pattern[i] == "I":
            while stack:
                res.append(stack.pop())
    return ''.join(map(str,res))
print(arrange_guest_arrival_order("IIIDIDDD"))
print(arrange_guest_arrival_order("DDD"))

'''
You are planning a special event where each attendee has a unique registration number. These numbers are listed in the provided array attendees, but they are currently out of order.

At the event, attendees will walk on stage one by one following this special reveal process:

The person at the front of the line walks on stage (this number is revealed).
If there are still people left in line, the next person in front moves to the back of the line.
Steps 1 and 2 repeat until everyone has walked on stage.
Your task is to rearrange the attendees list before the process starts so that the attendees walk on stage by registration number in increasing order.

Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, such that when the attendees follow the above reveal process they walk on stage from smallest registration number to largest registration number.

def reveal_attendee_list_in_order(attendees):
  pass
Example Usage:

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))
print(reveal_attendee_list_in_order([1,1000]))
Example Output:

[2,13,3,11,5,17,7]
[1,1000]

'''
from collections import deque


def reveal_attendee_list_in_order(attendees):
    attendeeList = sorted(attendees)
    n = len(attendees)
    res = [0] * n
    indices = deque(range(n))

    for attendee in attendeeList:
        index = indices.popleft()
        res[index] = attendee

        if indices:
            indices.append(indices.popleft())
    return res


print(reveal_attendee_list_in_order([17, 13, 11, 2, 3, 5, 7]))
print(reveal_attendee_list_in_order([1, 1000]))


"""
Problem 3: Arrange Event Attendees by Priority
You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, and an integer priority that indicates a particular level of priority.

Your task is to rearrange the attendees list such that the following conditions are met:

Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
Return the attendees list after the rearrangement.
"""
def arrange_attendees_by_priority(s, priority):
    # input : a integer list representing guests based off of their
    # priority level, and a arbitrary value of priority

    # output: an integer list partioned by where the guests level
    # are relative to if they are less
    # than or greater than the given priority

    # while loop to check l and r
    small = []
    eq = []
    big = []

    for i in range(len(s)):
        if s[i] > priority:
            big.append(s[i])
        elif s[i] == priority:
            eq.append(s[i])
        else:
            small.append(s[i])
    return small + eq + big


print(arrange_attendees_by_priority([9, 12, 5, 10, 14, 3, 10], 10))
print(arrange_attendees_by_priority([-3, 4, 3, 2], 2))
