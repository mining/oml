# -*- coding: utf-8 -*-
from quik import Template
from mining.utils import __from__

from .base import OMLBase


def ROW(name, func):
    try:
        return {name: func()}
    except:
        return {name: func}


def RunTime(language, items, OML):
    langruntime = __from__("oml.{}.RunTime".format(language.lower()))

    nitems = []
    for item in items:
        nitem = item.copy()
        for oml_line in OML.split("\n"):
            temp = Template(oml_line)
            render = temp.render(item)

            _run = langruntime.eval(
                """
                function(ROW, OML) return {} end
                """.format(render))
            nitem.update(_run(ROW, OMLBase()).items())
        nitems.append(nitem)
    return nitems
