# -*- coding: utf-8 -*-

from json import loads as load_json
import requests

class HttpClient(object):
    def get(self, url):
        return requests.get(url)

class NamedayRetriever(object):
    TODAY_BASE_URL = 'https://api.abalin.net/get/today?country={}'
    DATA_KEY = 'data'

    def __init__(self, http_client):
        self._client = http_client

    def today(self, country):
        response = self._client.get(self.TODAY_BASE_URL.format(country))
        return self._extract_names(response, country)

    def _extract_names(self, response, country):
        names_key = 'name_{}'.format(country)
        data = load_json(response)[self.DATA_KEY]
        return data[names_key]
