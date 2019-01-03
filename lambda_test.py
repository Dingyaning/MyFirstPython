from functools import reduce

lambda: True

lambda x, y: x + y

# 内建函数
# filter() map() reduce() zip()

a = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: x > 2, a)))

a=[1,2,3,4]
b=[4,5,6]
print(list(map(lambda x:x+1,a)))
print(list(map(lambda x,y:x+y,a,b)))

print(reduce(lambda x,y:x+y,[2,3,4],1))


for i in zip((1,2,3),(4,5,6)):
    print(i)

dicta = {'a':'aa','b':'bb'}
dictb = zip(dicta.values(),dicta.keys())
print(dict(dictb))

