"""
Notes:
    - Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.
Time Complexity:
    - Best	O(n2)
    - Worst	O(n2)
    - Average	O(n2)
Space Complexity: O(1)
"""

def selectionSort(array):
    size = len(array)
    
    for step in range(size):
        # set initial min index
        min_idx = step
        
        for i in range(step + 1, size):
            # Ascending order
            if array[i] < array[min_idx]:
                min_idx = i
        
        # swap (put minimum in current index)
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
print('Original Unsorted Array:')
print(data)
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)