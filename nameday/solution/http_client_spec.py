# -*- coding: utf-8 -*-

from datetime import datetime

from mamba import description, context, it
from expects import expect, be_true, have_key, equal

import nameday


TODAY_SPAIN_NAMEDAYS_URL = 'https://api.abalin.net/get/today?country=es'
SPAIN_NAMES_KEY = 'name_es'


with context('http client specs'):
    with before.each:
        self.http_client = nameday.HttpClient()

    with context('getting today\'s namedays for Spain'):
        with it('returns a valid response'):
            response = self.http_client.get(TODAY_SPAIN_NAMEDAYS_URL)

            expect(response.ok).to(be_true)

        with it('returns namedays for Spain'):
            response = self.http_client.get(TODAY_SPAIN_NAMEDAYS_URL)

            expect(response.json().get('data')).to(have_key(SPAIN_NAMES_KEY))

        with it('returns current day and month'):
            response = self.http_client.get(TODAY_SPAIN_NAMEDAYS_URL)

            now = datetime.now()
            expect(response.json().get('data').get('day')).to(equal(now.day))
            expect(response.json().get('data').get('month')).to(equal(now.month))
