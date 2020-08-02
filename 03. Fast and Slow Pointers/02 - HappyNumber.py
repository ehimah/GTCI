
def find_happy_number(num):
  slow, fast = num, num

  while True:
      slow = get_next_in_sequence(slow)
      fast = get_next_in_sequence(get_next_in_sequence(fast))

      if slow == fast:
          break

  return slow == 1

def get_next_in_sequence(num):
    sum_of_squares = 0
    while num > 0:
        sum_of_squares += (num % 10) ** 2
        num //= 10
    return sum_of_squares


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))

main()
