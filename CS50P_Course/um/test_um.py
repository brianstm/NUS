from um import count


def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM!") == 1


def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3
    assert count("Um? um, UM.") == 3


def test_um_as_substring():
    assert count("album") == 0
    assert count("yummy") == 0
    assert count("umbrella") == 0


def test_um_in_varied_contexts():
    assert count("Hello, um... how are you?") == 1
    assert count("UM, do you know where um, it is?") == 2
    assert count("Um thanks um") == 2
