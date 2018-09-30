from mamba import description, context, it
from expects import expect, equal

def fibonacci(index):
    if index < 2:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


with description('fibonacci specs'):
    with context('for index 0'):
        with it('has value 0'):
            index = 0

            value = fibonacci(index)

            expect(value).to(equal(0))

    with context('for index 1'):
        with it('has value 1'):
            index = 1

            value = fibonacci(index)

            expect(value).to(equal(1))

    with context('for index 2'):
        with it('has value 1'):
            index = 2

            value = fibonacci(index)

            expect(value).to(equal(1))

    with context('for index 3'):
        with it('has value 2'):
            index = 3

            value = fibonacci(index)

            expect(value).to(equal(2))

    with context('for index 4'):
        with it('has value 3'):
            index = 4

            value = fibonacci(index)

            expect(value).to(equal(3))

    with context('for index 17'):
        with it('has value 1597'):
            index = 17

            value = fibonacci(index)

            expect(value).to(equal(1597))
