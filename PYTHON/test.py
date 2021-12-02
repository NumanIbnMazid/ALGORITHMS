i = 0

for i in range(0, 23):
    if i == 15:
        break
    
print("The value of `i` is: ", i)

myArr = [j for j in range(0, 23)]

print(len(myArr) // 2, "ZZZZZZ", len(myArr))
for x in range(len(myArr) // 2, -1, -1):
    print('The value of `x` is: ', x)