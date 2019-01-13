# 带参数的装饰器

def tips(func):
    def nei(a, b):
        print('start')
        func(a, b)
        print('stop')

    return nei

def news_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' %(argv,func.__name__))
            func(a, b)
            print('stop')

        return nei
    return tips

@news_tips('add_module')
def add(a, b):
    print(a + b)


@news_tips('sub_module')
def sub(a, b):
    print(a - b)


print(add(4, 5))
print(sub(4, 5))

