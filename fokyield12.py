def foksiyon1():
    yield"Hello"
    yield 51
    yield "Good bye"
x = foksiyon1()
print(next(x))
print(next(x))
print(next(x))
