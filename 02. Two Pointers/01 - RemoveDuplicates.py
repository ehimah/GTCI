# coding: utf-8
""" 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
 """

def remove_duplicates(arr):
    nextNonDuplicateIndex = 1
    for i in range(len(arr))[1:]:
        if(arr[nextNonDuplicateIndex -1] != arr[i]):
            arr[nextNonDuplicateIndex] = arr[i]
            nextNonDuplicateIndex +=1

    return nextNonDuplicateIndex


"""  
Similar Questions #
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""
    
def remove_all_instances_of_element(arr, key):
    arraySize=0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[arraySize]=arr[i]
            arraySize += 1
    return arraySize


def main():
    print remove_duplicates([2,2, 3, 3, 3, 6, 9, 9])
    print remove_duplicates([2, 2, 2, 11])
    print remove_all_instances_of_element([3, 2, 3, 6, 3, 10, 9, 3], 3)
    print remove_all_instances_of_element([2, 11, 2, 2, 1], 2)
main()