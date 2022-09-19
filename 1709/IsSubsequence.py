s = "acb"
t = "ahbgdc"
# flag = True
# indexOfElement = 0
# for ele in s:
#     if ele in t:
#         if t.index(ele) >= indexOfElement:
#             indexOfElement = t.index(ele) + 1
#         else:
#             flag = False
#             break
#     else:
#         flag = False
#         break
# if flag:
#     print("subsequent")
# else:
#     print("not subsequent")
largeIndex = 0
flag = True
for idxS, eleS in enumerate(s):
    print('---')
    print('eleS: ', eleS)
    if eleS in t[largeIndex:]:
        for idxT in range(largeIndex,len(t)):
            print('eleT: ', t[idxT])
            if eleS == t[idxT]:
                print('char match')
                largeIndex = idxT + 1
                print('largeIndex: ', largeIndex)
                break
    else:
        print(eleS, 'not found in t')
        flag = False
        break
if flag:
    print("subsequent")
else:
    print("not subsequent")
