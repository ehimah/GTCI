from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def insert(intervals, new_interval):
    merged = []
    i = 0

    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1

    merged.append(new_interval)
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


def main():
    [i.print_interval(
    ) for i in insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6))]
    print()
    [i.print_interval() for i in insert(
        [Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10))]
    print()
    [i.print_interval()
     for i in insert([Interval(2, 3), Interval(5, 7)], Interval(1, 4))]
    print()
    


main()
