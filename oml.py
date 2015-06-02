# -*- coding: utf-8 -*-
import json
import requests
from urllib import urlencode
from quik import Template
from lupa import LuaRuntime


lua = LuaRuntime(unpack_returned_tuples=True)

OML = """ROW('new_collum1', SUM({@field1, @field2}))
ROW('new_collum2', SUBTRACT({@field1, @field2}))
ROW('geo', GEO_LOCATION("@address"))"""


def GEO_LOCATION(address):
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


def SUM(items):
    S = 0
    for i in range(1, len(items) + 1):
        S += items[i]
    return S


def SUBTRACT(items):
    S = 0
    for i in range(1, len(items) + 1):
        S -= items[i]
    return S


def ROW(name, func):
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
            function(ROW, SUM, SUBTRACT, GEO_LOCATION) return {} end
            """.format(render))
        nitem.update(_run(ROW, SUM, SUBTRACT, GEO_LOCATION).items())
    print nitem
