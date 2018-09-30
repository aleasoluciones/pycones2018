# -*- coding: utf-8 -*-

from mamba import description, context, it, before
from expects import expect, equal
from doublex import Spy, Stub, when
from doublex_expects import have_been_called_with

import nameday


A_COUNTRY = 'country'
TODAY_COUNTRY_NAMEDAYS_URL = 'https://api.abalin.net/get/today?country={}'.format(A_COUNTRY)
TODAY_COUNTRY_RESPONSE = '{"data":{"name_country":"Guido, Ciriaco, Paula","day":8,"month":9}}'


with description('nameday retriever specs'):
    with context('getting today\'s namedays for a specific country'):
        with before.each as self:
            self.http_client = Spy(nameday.HttpClient)
            when(self.http_client).get(TODAY_COUNTRY_NAMEDAYS_URL).returns(TODAY_COUNTRY_RESPONSE)
            self.nameday_retriever = nameday.NamedayRetriever(self.http_client)

        with it('calls http client with proper url'):
            _ = self.nameday_retriever.today(country=A_COUNTRY)

            expect(self.http_client.get).to(have_been_called_with(TODAY_COUNTRY_NAMEDAYS_URL))

        with it('returns the list of today\'s namedays for the country'):
            namedays = self.nameday_retriever.today(country=A_COUNTRY)

            expect(namedays).to(equal('Guido, Ciriaco, Paula'))
