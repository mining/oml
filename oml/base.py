# -*- coding: utf-8 -*-
import json
import requests
from urllib import urlencode


class OMLBase(object):

    def GEO_LOCATION(self, address):
        params = {
            'address': address,
            'sensor': 'false',
        }
        url = 'http://maps.google.com/maps/api/geocode/json?{}'.format(
            urlencode(params))
        req = requests.get(url)
        result = json.loads(req.text)
        try:
            return result['results'][0]['geometry']['location']
        except:
            return {}

    def SUM(self, items):
        S = 0
        for i in range(1, len(items) + 1):
            S += items[i]
        return S

    def SUB(self, items):
        S = 0
        for i in range(1, len(items) + 1):
            S -= items[i]
        return S


