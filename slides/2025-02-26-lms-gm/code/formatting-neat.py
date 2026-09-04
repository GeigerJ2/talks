import os
import sys


def foo(x, y):
    print(x + y)


class Bar:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def baz(self):
        return self.a * self.b


if __name__ == "__main__":
    foo(1, 2)
    b = Bar(3, 4)
    print(b.baz())
