# nums = [1, 2, 3, 4, 5]
# runningNum = []
# i = 0
# count = 0
# while i < len(nums)-1:
#     count = nums[i] + nums[i+1]
#     runningNum.append(count)
#     i += 1
# print(runningNum)

nums = [1, 2, 3, 4]
runningNum = []
total = 0

for i in range(len(nums)):
    total += nums[i]
    runningNum.append(total)
print(runningNum)