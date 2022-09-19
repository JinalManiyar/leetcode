low = 3
high = 7
# list1 = []
# for i in range(low, high + 1):
#     if i % 2 != 0:
#         list1.append(i)
# finalCount = len(list1)
# print(finalCount)

if low % 2 == 0:
    print((high - low + 1) // 2)
else:
    print((high - low) // 2 + 1)
