from simple_sum import simple_sum, simple_sub

def test_simple_sub():

    a = 5
    b = 6

    result = simple_sub(b, a)

    assert result == 1
    assert result != 0

def test_simple_sum():

    a = 5
    b = 6

    result = simple_sum(a, b)

    assert result == 11 
    assert result != 12
