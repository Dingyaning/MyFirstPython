# class Solution:
def twoSum(nums, target):
    length = len(nums)
    for i in range(length - 1):
        first = nums[i]
        for j in range(i + 1, length):
            second = nums[j]
            if first + second == target:
                return [i, j]


print(twoSum([1, 2, 3, 5], 5))

numV2 = {}


def twoSumV2(nums, target):
    for i in range(len(nums)):
        another_num = target - nums[i]
        if another_num in numV2:
            return [numV2[another_num], i]
        numV2[nums[i]] = i
    return None


print(twoSumV2([1, 2, 3, 5], 5))


# 闭包
def func():
    a = 1
    b = 2
    return a + b


def sum(a):
    def add(b):
        return a + b

    return add
# add 函数名称或函数的引用
# add() 函数调用


num1 = func()
print(type(num1))

num2 = sum(2)
print(type(num2))

print(num2(4))