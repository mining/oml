# -*- coding: utf-8 -*-
from quik import Template


def __from__(path):
    try:
        _import = path.split('.')[-1]
        _from = u".".join(path.split('.')[:-1])
        return getattr(__import__(_from, fromlist=[_import]), _import)
    except TypeError:
        return object


def ROW(name, func):
    try:
        return {name: func()}
    except:
        return {name: func}


def RunTime(language, items, OML, CLASS={"OML": "oml.base.OMLBase"}):
    langruntime = __from__("oml.{}.RunTime".format(language.lower()))

    for k in CLASS:
        CLASS[k] = __from__(CLASS[k])()
    CLASS["ROW"] = ROW

    nitems = []
    for item in items:
        nitem = item.copy()
        for oml_line in OML.split("\n"):
            temp = Template(oml_line)
            render = temp.render(item)

            runlang = Template(
                "function(#for @class in @_class:@class"
                "#if(@velocityHasNext), #end#end) "
                "return @render end")

            _run = langruntime.eval(runlang.render(
                {"_class": [i for i in CLASS],
                 "render": render}))
            nitem.update(_run(*CLASS.values()).items())
        nitems.append(nitem)
    return nitems
