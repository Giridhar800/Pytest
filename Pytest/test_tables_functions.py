import tables_functions as giri
import re

r = giri.print_tables(10) # this is generator object
r2 = list(r)   # converting generator object into a list

def test_length():
    assert len(r2) is 10

def test_type():
    assert type(r).__name__ == 'generator'

def test_using_regular_expression():
    for g in r2:
        assert re.match('([0-9]{1,2}.X.[0-9]{1,2}.=.[0-9]{1,2})',g)
        
