-- Added new collum1 field1 + field2
ROW('new_collum1', OML.SUM({@field1, @field2}))

-- Added new collum2 field1 - field2
ROW('new_collum2', OML.SUB({@field1, @field2}))

-- Added new field 'geo', find address on Google Maps
ROW('geo', OML.GEO_LOCATION("@address"))

-- Added new field 'func' string abc
ROW('func', function() return 'abc' end)

-- Added 2 new fields, 'dict1' field1*field2 and dict2 int 123
{dict1=@field1*@field2, dict2=123}
