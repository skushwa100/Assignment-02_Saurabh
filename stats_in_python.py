import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    """Read one numbered column from a text file and return its numbers and count."""
    # Keep the values from the requested column as we read the file line by line.
    values = []

    with open(filepath, 'r') as file:
        for line in file:
            # Split a line into separate columns, ignoring surrounding whitespace.
            data = line.strip().split()

            # Only convert the column when this line contains it.
            if len(data) > column:
                values.append(float(data[column]))

    # Return both the collected numbers and how many numbers were found.
    return values, len(values)


def calculate_average(numbers:list)->float:
    """Return the mean (sum divided by count), or 0.0 when the list is empty."""
    if len(numbers) == 0:
        return 0.0

    # Add all values and divide by the number of values.
    return sum(numbers) / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    """Return the largest and smallest numbers, in that order."""
    # Python's max and min find the two end values in the list.
    return max(numbers), min(numbers)

def calculate_variance(numbers:list)->float:
    """Return sample variance, which describes how spread out the numbers are."""
    # An empty list has no values to measure, so use 0.0 as its variance.
    if len(numbers) == 0:
        return 0.0

    # Measure each value's distance from the average.
    average = calculate_average(numbers)

    # With one value there is no spread, and n - 1 would be zero.
    if len(numbers) == 1:
        return 0.0

    # Square each distance so negatives do not cancel positives, add them, then
    # divide by n - 1 to calculate sample variance.
    variance = sum((x - average) ** 2 for x in numbers) / (len(numbers) - 1)

    return variance


def calculate_std_dev(numbers:list)->float:
    """Return standard deviation, the square root of the sample variance."""
    # Taking the square root puts the spread back in the same units as the data.
    return math.sqrt(calculate_variance(numbers))

def calculate_median(number:list)->float:
    """Return the middle value after sorting, or 0.0 when the list is empty."""
    if len(number) == 0:
        return 0.0

    # Sort a copy so the caller's original list remains unchanged.
    sorted_numbers = sorted(number)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        # For an even count, average the two values in the middle.
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    # For an odd count, return the single middle value as a float.
    return float(sorted_numbers[middle])

