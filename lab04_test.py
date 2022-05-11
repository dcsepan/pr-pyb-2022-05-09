 # teszteset == függvény
from lab04 import s_absolute ,  is_not_negativ

def test_with_negative_number():
    #given
     number = - 10
    #when
     result = is_not_negativ(number)
    #then 
     assert result == False


def test_with_positiv_number():
    #given
     number = 10
    #when
     result = is_not_negativ(number)
    #then 
     assert result == True

def test_with_zero():
    #given
     number = 0
    #when
     result = is_not_negativ(number)
    #then 
     assert result == True

def test_s_absolute_with_positiv():
    s = 10
    result = s_absolute(s)
    assert result == 10

def test_s_absolute_with_negativ():
    s = - 10
    result = s_absolute(s)
    assert result == -10