from mamba import description, context, it
from expects import expect, equal


def fibonacci(index):
    pass


with description('fibonacci specs'):
    with context('for index 0'):
        with it('has value 0'):
            index = 0

            value = fibonacci(index)

            expect(value).to(equal(0))
