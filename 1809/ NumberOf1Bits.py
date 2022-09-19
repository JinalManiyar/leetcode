import string
# n = 00000000000000000000000000001011
n = 1011
binary = "{0:32b}".format(n)
print(binary)
count = 0
for i in binary:
    if i == "1":
        count += 1
print(count)