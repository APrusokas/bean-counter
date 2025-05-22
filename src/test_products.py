from products import *

def test_neat_product_valid():
    input_tuple = (1, 'test drink', 9.99)
    expected = "1  -  test drink           £9.99"
    actual = neat_product(input_tuple)
    assert expected == actual

def test_neat_product_no_name():
    input_tuple = (1, '', 9.99)
    expected = "1  -                       £9.99"
    actual = neat_product(input_tuple)
    assert expected == actual

def test_neat_product_negative():
    input_tuple = (1, '', -9.99)
    expected = "1  -                       £-9.99"
    actual = neat_product(input_tuple)
    assert expected == actual