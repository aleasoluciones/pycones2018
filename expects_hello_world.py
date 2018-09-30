from mamba import description, context, it
from expects import expect, contain

with description('checking if string contains a character'):
    with context('given a character and a string'):
        with context('when the string contains the character'):
            with it('returns true'):
                character = 'C'
                string = 'PyConES2018'

                expect(string).to(contain(character))

        with context('when the string does NOT contain the character'):
            with it('return false'):
                character = 'x'
                string = 'PyConES2018'

                expect(string).not_to(contain(character))


