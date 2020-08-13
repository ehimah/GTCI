from __future__ import print_function

"""  
We'll have to segment the list into 3 parts
1. the segment before the sublist to be reversed
2. Sublist to be reversed
3. Segment after
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head
    current, previous = head, None

    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    end_of_first_segment = previous
    end_of_second_segment = current

    # now it's time to reverse the segment

    i, length_of_second_segment = 0, q - p + 1
    while current is not None and i < length_of_second_segment:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        i += 1
    # at the end of the reversal:
    # - current (the current start of 2nd segment) will the end of the reversed (2nd) segment
    # - previous (former end of the 1st segment) will be the start of the (2nd) segment
    end_of_first_segment.next = previous
    end_of_second_segment.next = current

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
