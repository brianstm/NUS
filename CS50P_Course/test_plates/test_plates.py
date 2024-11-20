from plates import is_valid


def test_length():
    assert is_valid("AB") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_with_letters():
    assert is_valid("1ABC") == False
    assert is_valid("AB123") == True
    assert is_valid("A1BCDE") == False
    assert is_valid("A12345") == False


def test_alphanumeric_only():
    assert is_valid("AB@123") == False
    assert is_valid("PLATE!") == False
    assert is_valid("ABC123") == True


def test_number_placement():
    assert is_valid("AB0123") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB123") == True
    assert is_valid("ABC123") == True


def test_edge_cases():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A0") == False
