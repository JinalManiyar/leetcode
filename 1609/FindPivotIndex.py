from typing import List


#
# leftMostIndex = 'hi'
#
# for i in range(len(nums)):
#     totalOfLeft = 0
#     totalOfRight = 0
#     print('value: ', nums[i])
#     for x in range(0, i):
#         totalOfLeft = totalOfLeft + nums[x]
#     print('totalOfLeft: ', totalOfLeft)
#     for y in range(i + 1, len(nums)):
#         totalOfRight = totalOfRight + nums[y]
#     print('totalOfRight: ', totalOfRight)
#     if totalOfLeft == totalOfRight:
#         leftMostIndex = i
#         break
#
# if leftMostIndex == 'hi':
#     print("left most index is: -1")
# else:
#     print("left most index is: ", leftMostIndex)

# leftMostIndex = null
#
# for i in nums:
#     left_sum = 0
#     right_sum = 0
#     for x in range(i-1...till 0):
#         left_sum = left_sum + x
#     for y in range(i+1...till list ends)
#         right sum = right_sum + y
#     if(left_sum == right_sum):
#         leftMostIndex = i
#         break
#
# if(leftMostIndex === null):
#     print(-1)
# else:
def pivotIndex(nums: List[int]) -> int:
    leftSum = 0
    rightSum = sum(nums)
    for idx, ele in enumerate(nums):
        print('num: ', nums[idx])
        rightSum = rightSum - ele
        print('rightSum: ', rightSum)
        if leftSum == rightSum:
            print('found pivot number: ', ele)
            return idx
        leftSum = leftSum + ele
        print('leftSum: ', leftSum)
    return -1


# nums = [-1, -1, 0, 0, -1, -1]
nums = [1, 7, 3, 6, 5, 6]
finalPivotIndex = pivotIndex(nums)
# print("Pivot Index: ", finalPivotIndex)
