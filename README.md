# Open Mining Language
Language to preprocess Olap Cubes


## Sample

DataSet:

    [
        {"nome": "Thiago Avelino", "field1": 10, "field2": 20, "address": "Av. Castelo Branco, 1300, Cacapava, SP, Brasil"},
        {"nome": "Luiz Vital", "field1": 30, "field2": 40, "address": "Cacapava, SP, Brasil"},
        {"nome": "Carlos Leite", "field1": 50, "field2": 60, "address": "Sao Jose dos Campos, SP, Brasil"}
    ]

OML:

    ROW('new_collum1', SUM({@field1, @field2}))
    ROW('new_collum2', SUBTRACT({@field1, @field2}))
    ROW('geo', GEO_LOCATION("@address"))

Return:

    {u'new_collum1': 30, u'new_collum2': -30, 'nome': 'Thiago Avelino', 'field2': 20, 'field1': 10, 'address': 'Av. Castelo Branco, 1300, Cacapava, SP, Brasil', u'geo': {u'lat': -23.1036861, u'lng': -45.7197228}}
    {u'new_collum1': 70, u'new_collum2': -70, 'nome': 'Luiz Vital', 'field2': 40, 'field1': 30, 'address': 'Cacapava, SP, Brasil', u'geo': {u'lat': -23.0996965, u'lng': -45.7080824}}
    {u'new_collum1': 110, u'new_collum2': -110, 'nome': 'Carlos Leite', 'field2': 60, 'field1': 50, 'address': 'Sao Jose dos Campos, SP, Brasil', u'geo': {u'lat': -23.223701, u'lng': -45.9009074}}


## TODO

- [x] Run lua
- [ ] Run R (We spent a day doing a proof of concept and we can't use simply as Moon, let's start the project with Moon after we returned in R)
