""" 
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""

def make_squares(arr):
    squares = [] #or collections.deque()
    left = 0
    right = len(arr) - 1
    while(left <= right):
        if arr[left]**2 > arr[right]**2:
            squares.insert(0, arr[left]**2) #or squares.appendleft(arr[left]**2)
            left += 1
        else:
            squares.insert(0, arr[right] ** 2)
            right -= 1

    return squares


def main():
    print list(make_squares([-2, -1, 0, 2, 3]))
    print list(make_squares([-3, -1, 0, 1, 2]))

main()