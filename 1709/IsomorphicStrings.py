s = "badc"
t = "baba"
if len(s) != len(t):
    print("not  aisomorphic")
dict1 = {}
flag = 0
for idx, ele in enumerate(s):
    if ele not in dict1:
        if t[idx] not in dict1.values():
            dict1[ele] = t[idx]
        else:
            flag = False
            break
    print(dict1)
    if dict1[ele] == t[idx]:
        flag = True
    else:
        flag = False
        break
print(dict1)
if flag:
    print("isomorphic")
else:
    print("not isomorphic")
