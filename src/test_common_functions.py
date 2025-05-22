from common_functions import *

def test_blue_valid():
    input_text = "test this"
    expected = "\033[36mtest this\033[0m"
    actual = blue(input_text)
    assert expected == actual

    
def test_blue_number():
    input_text = 34
    expected = "\033[36m34\033[0m"
    actual = blue(input_text)
    assert expected == actual

def test_blue_tuple():
    input_text = (1, 2, 3)
    expected = "\033[36m(1, 2, 3)\033[0m"
    actual = blue(input_text)
    assert expected == actual

def test_blue_empty():
    input_text = ""
    expected = "\033[36m\033[0m"
    actual = blue(input_text)
    assert expected == actual