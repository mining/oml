#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from oml import RunTime


class InitialTest(TestCase):
    def setUp(self):
        self.dataset = [
            {"nome": "Thiago Avelino", "field1": 10, "field2": 20,
             "address": "Av. Castelo Branco, 1300, Cacapava, SP, Brasil"},
            {"nome": "Luiz Vital", "field1": 30, "field2": 40,
             "address": "Cacapava, SP, Brasil"},
            {"nome": "Carlos Leite", "field1": 50, "field2": 60,
             "address": "Sao Jose dos Campos, SP, Brasil"}
        ]

    def test_multi_ROW(self):

        OML = """ROW('new_collum1', OML.SUM({@field1, @field2}))
        ROW('new_collum2', OML.SUB({@field1, @field2}))
        ROW('geo', OML.GEO_LOCATION("@address"))
        ROW('func', function() return 'abc' end)
        {dict1=@field1*@field2, dict2=123}"""

        run = RunTime("lua", self.dataset, OML)
        self.assertTrue(run)
        self.assertEqual(len(run), 3)

    def test_set_CLASS(self):

        OML = """ROW('new_collum1', TEST.SUM({@field1, @field2}))
        ROW('new_collum2', TEST.SUB({@field1, @field2}))
        ROW('geo', TEST.GEO_LOCATION("@address"))"""

        run = RunTime("lua", self.dataset, OML, {"TEST": "oml.base.OMLBase"})
        self.assertTrue(run)
        self.assertEqual(len(run), 3)


if __name__ == '__main__':
    unittest.main()
