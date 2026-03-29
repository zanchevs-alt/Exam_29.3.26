
import statistics

def find_median(numbers: list) -> float:
    """
    find the median of a list
    :param numbers: sorted_list - list of numbers by order
    :return: median
    """
    sorted_list = sorted(numbers)
    print(sorted_list)
    return statistics.median(numbers)

numbers = [3, 1, 4, 1, 5]
print(find_median(numbers))
numbers = [7, 2, 10, 9]
print(find_median(numbers))
numbers = [42]
print(find_median(numbers))


