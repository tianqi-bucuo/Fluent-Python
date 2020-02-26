def f(name):

    def g(instance):
        return instance.__dict__[name]

    def s(instance, value):
        if value > 0:
            instance.__dict__[name] = value
        else:
            raise ValueError('value must be > 0')
    return property(g, s)   # 关键在于property函数


class L:
    weight = f('weight')

    def __init__(self, weight):
        self.weight = weight


l = L(8)

