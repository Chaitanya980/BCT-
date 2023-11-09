import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = []
    right = []

    for i, element in enumerate(arr):
        if i == pivot_index:
            continue
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

# Generate a random list of integers
arr = [random.randint(1, 1000) for _ in range(10)]

# Copy the list to keep the original unsorted list
deterministic_sorted = deterministic_quick_sort(arr.copy())
randomized_sorted = randomized_quick_sort(arr.copy())

# Print the original and sorted lists
print("Original List: ", arr)
print("Deterministic Quick Sort: ", deterministic_sorted)
print("Randomized Quick Sort: ", randomized_sorted)

# Measure the time taken for each variant
start_time = time.time()
deterministic_quick_sort(arr.copy())
deterministic_time = time.time() - start_time

start_time = time.time()
randomized_quick_sort(arr.copy())
randomized_time = time.time() - start_time

print("Deterministic Quick Sort Time: {:.6f} seconds".format(deterministic_time))
print("Randomized Quick Sort Time: {:.6f} seconds".format(randomized_time))