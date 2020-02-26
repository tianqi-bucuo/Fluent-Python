class LineItem:
    def __init__(self, description, price):
        self.description = description
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.weight
