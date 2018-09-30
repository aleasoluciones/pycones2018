from mamba import description, context, it
from expects import expect, equal


def fibonacci(index):
    if index < 2:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


with description('fibonacci specs'):
    with context('for the first two indexes'):
        with it('returns index'):
            expected_values = {0: 0, 1: 1}
            for index, expected_value in expected_values.items():
                value = fibonacci(index)

                expect(value).to(equal(expected_value))

    with context('for the rest of indexes'):
        with it('returns the sum of the previous two values'):
            expected_values = {2: 1,
                               3: 2,
                               4: 3,
                               5: 5,
                               6: 8,
                               17: 1597,}
            for index, expected_value in expected_values.items():
                value = fibonacci(index)

                expect(value).to(equal(expected_value))
