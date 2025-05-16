class basic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculation(self, a, b):
        add = self.a + self.b
        sub = self.a - self.b
        mul = self.a * self.b
        div = self.a / self.b
        return f"add: {add}\nsub: {sub}\nMul: {mul}\ndiv: {div:.2f}"

class Child(basic):
    def calc(self, a, b):
       add, sub, mul, div = self.calculation(a, b)
       return f"add: {add}\nsub: {sub}\nMul: {mul}\ndiv: {div:.2f}"

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
child = Child(a, b)
print(child.calculation(a, b))
