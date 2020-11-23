from functools import reduce

def prod(list):
    def func(x, y):
        return x * y
    return reduce(func, list)

# 测试
print('1 * 2 * 3 * 4 =', prod([1,2, 3, 4]))
if prod([1,2, 3, 4]) == 24:
    print('success!')
else:
    print('fail!')