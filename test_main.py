from main import i_return_four


def test_i_return_four():
    """The test mistanenly correctly asserts four.
    """
    res = i_return_four()
    assert res == 4