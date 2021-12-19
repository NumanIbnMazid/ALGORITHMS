"""
Notes:
    - Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
    - Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.
Time Complexity:
    - Best Case Complexity: O(n*log n)
    - Worst Case Complexity: O(n*log n)
    - Average Case Complexity: O(n*log n)
Space Complexity:
    - The space complexity of merge sort is O(n).
"""

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # recusively call mergeSort on the left and right halves
        mergeSort(left)
        mergeSort(right)

        # iterator for traversing the two halves
        i = 0
        j = 0
        # iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left has been used
                myList[k] = left[i]
                # move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # move to the next slot in the main list
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
            

myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)
