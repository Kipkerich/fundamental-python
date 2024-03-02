import double


def test_fn():
    assert double.double_int(4) == 8
    assert double.double_string("cat") == "catcat"