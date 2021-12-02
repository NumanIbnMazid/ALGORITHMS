
myArr = [100, 90, 110, 110, 50, 20, 70, 40, 10]

for i in range(0, len(myArr) - 1):
    for j in range(0, len(myArr) - i - 1):
        if myArr[j] > myArr[j + 1]:
            myArr[j], myArr[j + 1] = myArr[j + 1], myArr[j]

print(myArr)

print([[], ] * 10)

print("test 2 \n")


n = 50
for i in range(2, n//2):
    print(i, " -X")
    
print(" - Hash -")
print(hash(23))
print(hash("ABC") % 100)