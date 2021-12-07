"""
Notes:
    - Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.
    - Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration. Therefore, it is called a bubble sort.
Time Complexity:
    - Best	O(n)
    - Worst	O(n2)
    - Average	O(n2)
    - Space Complexity	O(1)
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            # compare between two adjacent and swap them if required
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

print("\n ------- Optimized Bubble Sort ------- \n")

def bubbleSort(array):
    for i in range(len(array)):
        
        swapped = False
        
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        
        if not swapped:
            break
        

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
