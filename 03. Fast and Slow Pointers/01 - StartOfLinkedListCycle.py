from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    # 1. find cycle length
    slow_ptr, fast_ptr = head, head
    cycle_length = 0
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            cycle_length = calculate_cycle_length(slow_ptr)
            break
    return find_cycle_head(head, cycle_length)


def calculate_cycle_length(start_ptr):
    current = start_ptr
    cycle_length = 0
    while True:
        start_ptr = start_ptr.next
        cycle_length += 1
        if current == start_ptr:
            break
    return cycle_length

def find_cycle_head(head, cycle_length):
    # 2. find start of cycle by incrementing fast ptr by K nodes and iterating till both pointers meet
    left_ptr, right_ptr = head, head

    while cycle_length > 0:
        right_ptr = right_ptr.next
        cycle_length -= 1
    
    while left_ptr != right_ptr:
        left_ptr = left_ptr.next
        right_ptr = right_ptr.next
    return left_ptr

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()
