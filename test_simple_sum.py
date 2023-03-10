from simple_sum import simple_sum

def test_simple_sum():

    a = 5
    b = 6

    result = simple_sum(a, b)

    assert result == 11 
    assert result != 12