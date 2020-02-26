# import heartrate; heartrate.trace(browser=True)


class B:
    def __len__(self):
        return 2

    def __str__(self):
        return 'a'


b = B()
print(len('qqqqq'))
print(len(b))
print(str(b))
print(str(1))


class A:
    def __init__(self):
        print('init function')

    def __new__(cls, *args, **kwargs):
        print('new function')
        return object.__new__(A)


a = A()
s1 = 'xxx'
s2 = s1.encode('utf-8')

print(s1, type(s1))
print(s2, type(s2))

Matrix_c = [[] for i in range(3)]
Matrix_c[0].append(1)
print(Matrix_c)
