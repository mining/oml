# -*- coding: utf-8 -*-
import json
import requests
from urllib import urlencode
from quik import Template
from lupa import LuaRuntime


lua = LuaRuntime(unpack_returned_tuples=True)

OML = """ROW('new_collum1', OML.SUM({@field1, @field2}))
ROW('new_collum2', OML.SUB({@field1, @field2}))
ROW('geo', OML.GEO_LOCATION("@address"))
ROW('func', function() return 'abc' end)
{dict1=@field1*@field2, dict2=123}"""


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


def ROW(name, func):
    try:
        return {name: func()}
    except:
        return {name: func}


items = [
    {"nome": "Thiago Avelino", "field1": 10, "field2": 20,
     "address": "Av. Castelo Branco, 1300, Cacapava, SP, Brasil"},
    {"nome": "Luiz Vital", "field1": 30, "field2": 40,
     "address": "Cacapava, SP, Brasil"},
    {"nome": "Carlos Leite", "field1": 50, "field2": 60,
     "address": "Sao Jose dos Campos, SP, Brasil"}
]

for item in items:
    nitem = item.copy()
    for oml_line in OML.split("\n"):
        temp = Template(oml_line)
        render = temp.render(item)

        _run = lua.eval(
            """
            function(ROW, OML) return {} end
            """.format(render))
        nitem.update(_run(ROW, OMLBase()).items())
    print(nitem)
