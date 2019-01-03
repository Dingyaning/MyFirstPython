# 迭代器
# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# for i in range(10, 20, 2):
#     print(i)


def frang(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frang(10, 20, 0.5):
    print(i)
