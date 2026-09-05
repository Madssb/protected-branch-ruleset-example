from main import i_return_four


def test_i_return_four():
    """The test mistanenly asserts five.
    """
    res = i_return_four()
    assert res == 5