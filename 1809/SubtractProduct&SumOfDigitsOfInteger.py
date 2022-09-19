import math

n = 234
multiplyVal = 1
addVal = 0
while n > 0:
    sepValue = n % 10
    n = math.floor(n / 10)
    multiplyVal = multiplyVal * sepValue
    addVal = addVal + sepValue
print(multiplyVal - addVal)
