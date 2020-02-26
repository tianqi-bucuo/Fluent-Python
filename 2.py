class A():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class B(A):
    def __init__(self, x, y):
        super(B, self).__init__(x, y)

b = B(1,2)