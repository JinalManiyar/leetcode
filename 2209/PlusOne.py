digits = [9,9]
# addedString = ""
# for i in digits:
#     addedString = addedString + str(i)
# addedNum = str(int(addedString) + 1)
# listNum = []
# for i in addedNum:
#     listNum.append(int(i))
# print(listNum)

# lenOfDigits = len(digits)
# if digits[lenOfDigits - 1] == 9:
#     print("hi")
#     my_list = [int(x) for x in str(digits[lenOfDigits - 1] + 1)]
#     if lenOfDigits ==1:
#         print(my_list)
#     else:
#         digits[lenOfDigits - 1] = my_list[1]
#         digits[lenOfDigits - 2] = digits[lenOfDigits - 2] + my_list[0]
#         print(digits)
# else:
#     my_list = [int(x) for x in str(digits[lenOfDigits - 1] + 1)]
#     digits[lenOfDigits - 1] = my_list[0]
#     print(digits)
pointer = len(digits) - 1

while digits[pointer] == 9:
    digits[pointer] = 0
    pointer -= 1

if pointer == -1:
    digits.insert(0, 1)

else:
    digits[pointer] += 1

print(digits)