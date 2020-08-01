
def triplet_sum_close_to_target(arr, target_sum):
    minimum_absolute_difference = float('inf')
    closest_sum = 0
    for i in range(len(arr)-1):
        index = i + 1
        while index < len(arr)-1:
            current_sum = arr[i] + arr[index] + arr[index+1]
            minimum_absolute_difference = min(
                minimum_absolute_difference, abs(target_sum - current_sum))
            index += 1

    return minimum_absolute_difference


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
