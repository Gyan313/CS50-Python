from calculator import square
import pytest

def main():
    test_positive()
    test_negative()
    test_zero()

def test_positive():
    # try:
    #     assert square(2)==4 #corner case
    # except AssertionError:
    #     print("square of 2 is not 4")
    # try:
    #     assert square(-2)==4
    # except AssertionError:
    #     print("square of -2 is not 4")
    # try:
    #     assert square(-3)==9
    # except AssertionError:
    #     print("square of -3 is not 9")
    # test_negative()
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("a")

if __name__=="__main__":
    main()

    