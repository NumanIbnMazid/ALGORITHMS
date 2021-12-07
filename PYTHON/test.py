
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

myArr = [1, 2, 3, 4, 5, 6, 7]

for i in range(0, len(myArr)):
    for j in range(0, len(myArr) - i - 1):
        print(myArr[i], myArr[j])
