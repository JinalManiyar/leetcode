nums = [1, 3, 5, 6]
target = 0
foundPosition = False
for idx, ele in enumerate(nums):
    if ele >= target:
        print(idx)
        foundPosition = True
        break

if not foundPosition:
    print(len(nums))

# ---------------------
# for i in nums:
#     if i >= target:
#         return nums.index(i)
# if target not in nums:
#     return len(nums)
