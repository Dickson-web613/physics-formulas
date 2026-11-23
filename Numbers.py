# Function 1: Calculate the sum
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function 2: Calculate the mean (average)
def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0

    return calculate_sum(numbers) / len(numbers)


# Function 3: Calculate the median and mode
def calculate_median_mode(numbers):
    if len(numbers) == 0:
        return None, None

    # Sort the list
    sorted_numbers = sorted(numbers)

    # Calculate median
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        median = sorted_numbers[middle]

    # Calculate mode
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    highest_frequency = max(frequency.values())
    mode = [num for num, count in frequency.items()
            if count == highest_frequency]

    return median, mode


# Test the functions
numbers = [2, 4, 4, 6, 8, 10, 10, 10]

print("Sum:", calculate_sum(numbers))
print("Mean:", calculate_mean(numbers))

median_value, mode_value = calculate_median_mode(numbers)

print("Median:", median_value)
print("Mode:", mode_value)