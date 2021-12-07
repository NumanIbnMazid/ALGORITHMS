
# import fractions


# def percent_to_fraction(percent_number):
#     decimal_number = percent_number / 100
#     fraction = fractions.Fraction(decimal_number)
#     return fraction


# percent_input = 75
# fraction_output = percent_to_fraction(percent_input)
# print('fraction result is:{0}'.format(fraction_output))

# def findOdd(lowerBound, upperBound):
#     totalNumberOfOddNumbers = 0
#     for i in range(lowerBound, upperBound + 1):
#         if (i % 2 != 0):
#             totalNumberOfOddNumbers += 1
#     return totalNumberOfOddNumbers


# print(findOdd(1, 10))
# print(findOdd(2, 15))

# myList = []
# size = 10
# for i in range(size):
#     myList.append([0 for i in range(size)])
# print(myList)


# print(set({"1":"2"}))

# print({'1', '2'} - {'1'})

# import collections

# queue = collections.deque([1, 3, 4, 5])
# print(queue)

# myArr = [1, 2, 3, 4, 5, 6, 7]

# for i in range(0, len(myArr)):
#     for j in range(0, len(myArr) - i - 1):
#         print(myArr[i], myArr[j])


myMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def get_result(matrix):
    result = []

    preRes = []

    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            preRes.append([matrix[i], matrix[j]])
    
    def recursion(arr1, arr2):
        for i in arr1:
            pre = []
            for j in arr2:
                pre.append(i + " " + j)
            result.append(pre)
                
    for arr in preRes:
        recursion(arr1=arr[0], arr2=arr[-1])

    return result


myMatrix = [
    ["Red", "Blue", "Black"],
    ["A", "B", "C"],
    ["1", "2", "3"]
]

# myMatrix = [
#     ["Red", "Blue"],
#     ["S", "M"]
# ]

print(get_result(myMatrix))

# myMatrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# display = [
#     [4, 5, 6], 
#     [8, 10, 12], 
#     [12, 15, 18], 
#     [7, 8, 9], 
#     [14, 16, 18], 
#     [21, 24, 27], 
#     [28, 32, 36], 
#     [35, 40, 45], 
#     [42, 48, 54]
# ]

display = [
    ['Red A', 'Red B', 'Red C'], 
    ['Blue A', 'Blue B', 'Blue C'], 
    ['Black A', 'Black B', 'Black C'], 
    ['Red 1', 'Red 2', 'Red 3'], 
    ['Blue 1', 'Blue 2', 'Blue 3'], 
    ['Black 1', 'Black 2', 'Black 3'], 
    ['A 1', 'A 2', 'A 3'], 
    ['B 1', 'B 2', 'B 3'], 
    ['C 1', 'C 2', 'C 3']
]
