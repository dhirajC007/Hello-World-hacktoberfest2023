def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: an empty list or a list with a single element is already sorted

    pivot = arr[0]  # Choose a pivot element (can be any element in the list)
    less_than_pivot = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to the pivot
    greater_than_pivot = [x for x in arr[1:] if x > pivot]  # Elements greater than the pivot

    # Recursively sort the sublists and combine them
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = quick_sort(my_list)
print("Sorted array:", sorted_list)
